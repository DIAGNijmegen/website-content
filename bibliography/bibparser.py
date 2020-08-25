import json
import time
import latexcodec
import codecs
import glob
import os
import numpy as np

from mdfiles import create_author_md_files, create_publication_md, create_group_md_files
from authors import get_list_researchers, get_publications_by_author
from bibreader import parse_bibtex_file


class SetEncoder(json.JSONEncoder):
    def default(self, obj):
       if isinstance(obj, set):
          return list(obj)
       return json.JSONEncoder.default(self, obj)

def save_dict2json(json_path, dict_md5):
    with open(json_path, 'w') as fp:
        json.dump(dict_md5, fp, cls=SetEncoder, ensure_ascii=False)


def load_json2dict(json_path):
    if os.path.exists(json_path):
        json_file = open(json_path)
        json_data = json.load(json_file)
    else:
        json_data = None
    return json_data


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r ran for  %2.2f ms' %
                  (method.__name__, (te - ts) * 1000))
        return result
    return timed


def sort_bib_keys_author(author_bib_keys, bib_items):
    _types = ['article', 'preprint', 'inproceedings', 'conference', 'phdthesis', 'mastersthesis', 'book', 'other']
    bib_items_per_author_per_date = {}
    for researcher, keys in author_bib_keys.items():
        bib_items_per_data = {}
        for key in keys:
            bib_items_per_data.setdefault(bib_items[key]['year'], set()).add(key)
            bib_items_per_data.setdefault('__types__', set()).add(bib_items[key]['type'])
        bib_items_per_data['__years__'] = sorted(set([y for y in bib_items_per_data.keys() if isinstance(y, int)]))[::-1]
        bib_items_per_data['__types__'] = [t for t in _types if t in bib_items_per_data['__types__']]

        #TODO sort by month
        bib_items_per_author_per_date[researcher] = bib_items_per_data
    return bib_items_per_author_per_date


def sort_bib_keys_group(author_bib_keys, bib_items, list_researchers):
    _types = ['article', 'preprint', 'inproceedings', 'conference', 'phdthesis', 'mastersthesis', 'book', 'other']
    bib_items_per_group_per_date = {}
    groups = []
    publication_types = set()
    for researcher, keys in author_bib_keys.items():
        # set group if not set
        for group in list_researchers[researcher][1]:
            if group not in groups:
                groups.append(group)
            bib_items_per_group_per_date.setdefault(group, {})
            for key in keys:
                bib_items_per_group_per_date[group].setdefault(bib_items[key]['year'], set()).add(key)
                bib_items_per_group_per_date[group].setdefault('__types__', set()).add(bib_items[key]['type'])
                
    # compute all years per group
    for group in groups:
        bib_items_per_group_per_date[group]['__years__'] = sorted(set([y for y in bib_items_per_group_per_date[group].keys() if isinstance(y, int)]))[::-1]
        bib_items_per_group_per_date[group]['__types__'] = [t for t in _types if t in bib_items_per_group_per_date[group]['__types__']]
        #TODO sort by month
    return bib_items_per_group_per_date


@timeit
def parse_bib_file():
    print('parsing bib file...')
    bib_items = parse_bibtex_file('/home/mart/Radboudumc/diag-literature/diag.bib', '/home/mart/Radboudumc/diag-literature/fullstrings.bib')
    
    print('retreiving list of diag members')
    list_researchers = get_list_researchers('./content/pages/members/')

    print('mapping bib keys to authors')
    author_bib_keys = get_publications_by_author(bib_items, list_researchers)

    # sorting
    print('sorting')
    bib_items_per_author_per_date = sort_bib_keys_author(author_bib_keys, bib_items)
    bib_items_per_group_per_date = sort_bib_keys_group(author_bib_keys, bib_items, list_researchers)

    # saving
    print('saving bibitems.json')
    save_dict2json('./content/bibitems.json', bib_items)
    print('saving authorbibkeys.json')
    save_dict2json('./content/authorkeys.json', bib_items_per_author_per_date )
    print('saving groupbibkeys.json')
    save_dict2json('./content/groupkeys.json', bib_items_per_group_per_date )

    return bib_items, list_researchers, bib_items_per_author_per_date, bib_items_per_group_per_date


if __name__ == "__main__":
    bib_items, list_researchers, bib_items_per_author_per_date, bib_items_per_group_per_date = parse_bib_file()

    print('creating author md files')
    create_author_md_files(bib_items_per_author_per_date, list_researchers)

    print('creating group md files')
    create_group_md_files(bib_items_per_group_per_date)

    print('creating publication md files')
    create_publication_md(bib_items, bib_items_per_author_per_date, list_researchers)

    
