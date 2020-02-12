import json
import time
import latexcodec
import codecs
import glob
import os 


from mdfiles import create_author_md_files, create_publication_md
from authors import get_list_researchers, get_publications_by_author
from bibreader import parse_bibtex_file


def save_dict2json(json_path, dict_md5):
    with open(json_path, 'w') as fp:
        json.dump(dict_md5, fp)


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
            print('%r ran for  %2.2f ms' % \
                  (method.__name__, (te - ts) * 1000))
        return result
    return timed

@timeit
def parse_bib_file():
    print('parsing bib file...')
    bib_items = parse_bibtex_file('./content/diag.bib')
    print('retreiving list of diag members')
    list_researchers = get_list_researchers('./content/pages/members/')  
    print('mapping bib keys to authors')
    author_bib_keys = get_publications_by_author(bib_items, list_researchers)
    print('saving bibitems.json')
    save_dict2json('./content/bibitems.json', bib_items)
    print('saving auhtorbibkeys.json')
    save_dict2json('./content/authorkeys.json', author_bib_keys)

    return bib_items, list_researchers, author_bib_keys


if __name__ == "__main__":
    bib_items, list_researchers, author_bib_keys = parse_bib_file()
    print('creating author md files')
    create_author_md_files(author_bib_keys, list_researchers)
    print('creating publication md files')
    create_publication_md(bib_items, author_bib_keys, list_researchers)
    	
