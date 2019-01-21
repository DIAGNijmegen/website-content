"""
This plugin writes the md files for each publication found in bib_file (diag.bib by default)
It writes the output in 'out_dir'

@author Gabriel (ghumpire)
"""
import os
import glob
import json
import time
import hashlib
import _pickle as pickle
import codecs
import latexcodec

from bibtex import bibtexlib
from bibtex import bibtexformatter


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


def get_publications_by_author(global_index, list_researchers):
    from collections import defaultdict
    author_index = defaultdict(set)
    filtered_publications = []

    for bib_key, bib_item in global_index.items():
        authors = bib_item.author

        for researcher_names in list_researchers:
            firstname = researcher_names[0]
            lastname = researcher_names[-1]
            for first, von, last, jr in authors:
                if last.lower() == lastname and first[0].lower() == firstname[0].lower():
                    author_index[lastname].add(bib_key)
                    # Some 'von' are actually lastnames
                    pvon = von.replace(' ', '').replace('.', '')

                    if len(pvon) > 3:
                        author_index[von].add(bib_key)
                    if bib_key not in filtered_publications:
                        filtered_publications.append(bib_key)

    return author_index, filtered_publications


def generate_md_bibitem():
    """ Uses the Bart's bibtex script to write the following markdown files:
        - content/Publications.md that contains the full list of publications
        - A MD file for every publication (filtered by researcher name)
        - A list of publications per researcher on content/pages/members/*.md with the same slug
          on content/pages/publications. For instance content/pages/publications/francesco-ciompi.md
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))

    out_dir = os.path.join(base_dir, '..', 'content/pages/publications')
    bib_file = os.path.join(base_dir, '..', 'content/diag.bib')
    json_path = os.path.join(base_dir, '..', 'output/md5s.json')

    print('Bibtex plugin loaded')
    print('Output dirs: {}'.format((out_dir, bib_file, json_path)))

    start_time = time.clock()
    index, global_index, string_rules = bibtexlib.read_bibtex_file(bib_file)
    time_diagbib = time.clock() - start_time
    start_time = time.clock()

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    list_researchers = get_list_people()
    author_index, filtered_publications = get_publications_by_author(global_index, list_researchers)

    write_single_publication_md(global_index, string_rules, filtered_publications, out_dir, json_path)
    print('\nTime to process diag.bib ', time_diagbib)
    print('Time to create ' + str(len(global_index)) + ' MD files ', time.clock() - start_time)

    time_list_pubs = time.clock()
    write_author_publications_md(global_index, author_index, list_researchers, out_dir, string_rules)
    dict_pubs = write_list_publications_md(global_index, filtered_publications, out_dir, string_rules)
    print('Time to create filtered list of publications and publications per researcher', time.clock() - time_list_pubs)
    json_path = os.path.join(base_dir, '..', 'content/dict_pubs.json')
    save_dict2json(json_path, dict_pubs)

    
def append_publication_md(global_index, bib_key, html_format, go_parent_dir=False):
    bib_item = global_index[bib_key]
    html_to_write, pub_details = html_format.apply(bib_item)
    pub_html = '<li>'
    pub_html += html_to_write
    pub_html += r'. <a href="{filename}/pages/publications/' + bib_key.lower() + r'.md">Abstract</a>'

    pub_type = bib_item.entry_type
    if 'year' in bib_item.entry:
        year = bib_item.entry['year']
    else:
        # If year is absent, the bib_key is used to set the year
        year = int(bib_key[-2:])
        year = 2000 + year if year < 50 else 1900 + year

    if 'doi' in bib_item.entry:
        url_doi = 'https://doi.org/' + bib_item.entry['doi']
        pub_html += ' <a href=\"' + url_doi + '\">DOI</a>'
    if 'url' in bib_item.entry and 'arxiv' in bib_item.entry['url']:
        url_arxiv = bib_item.entry['url']
        pub_html += ' <a href=\"' + url_arxiv + '/\">arXiv</a>'
    if 'pmid' in bib_item.entry:
        url_pmid = 'http://www.ncbi.nlm.nih.gov/pubmed/' + bib_item.entry['pmid']
        pub_html += ' <a href=\"' + url_pmid + '/\">PMID</a>'

    pub_html += '</li>\n'

    return pub_html, year, pub_type, pub_details


def write_md_pass(out_path, md_format):
    file = open(out_path, 'w', encoding='utf-8')

    try:  # This is ugly but necessary for now to avoid UnicodeEncodeError
        file.write(md_format)
        file.close()
    except UnicodeEncodeError:
        pass


def write_list_publications_md(global_index, filtered_publications, out_dir, string_rules):
    html_format = bibtexformatter.HTML_Formatter(string_rules)

    dict_pubs = {}
    for bib_key in filtered_publications:
        bib_key = bib_key.lower()
        html_bibkey, year, pub_type, pub_details = append_publication_md(global_index, bib_key, html_format, go_parent_dir=False)
        dict_pubs[bib_key] = {}
        dict_pubs[bib_key]['html'] = html_bibkey
        dict_pubs[bib_key]['year'] = int(year)
        dict_pubs[bib_key]['pub_type'] = pub_type
        dict_pubs[bib_key]['pub_details'] = pub_details
        if pub_type.lower() == '@phdthesis':
            dict_pubs[bib_key]['author_name'] = global_index[bib_key].entry['author']
            dict_pubs[bib_key]['title_thesis'] = global_index[bib_key].entry['title']
            # TODO this is a hardcode capital first letter of bibkey
            dict_pubs[bib_key]['coverpng'] = bib_key[0].title()+bib_key[1:]+'.png'
    return dict_pubs


def write_author_publications_md(global_index, author_index, list_researchers, out_dir, string_rules):
    list_bibs_error = []
    html_format = bibtexformatter.HTML_Formatter(string_rules)

    for researcher_names in list_researchers:
        full_name = "-".join(researcher_names)
        title_md = " ".join(researcher_names).title()  # camel case
        md_format = 'title: Publications of ' + title_md + '\n'
        md_format += 'template: publications-author\n'
        md_format += 'author: ' + "-".join(researcher_names) + '\n'
        md_format += 'author_name: ' + title_md + '\n'
        list_pubs_author = []
        for author_name in author_index.keys():
            if researcher_names[-1] == author_name.lower():
                for bib_key in author_index[author_name]:
                    list_pubs_author.append(bib_key)
        md_format += 'bibkeys: '+','.join(list_pubs_author)

        out_path = os.path.join(out_dir, full_name + '.md')

        write_md_pass(out_path, md_format)


def write_single_publication_md(global_index, string_rules, filtered_publications, out_dir, json_path):
    html_format = bibtexformatter.HTML_Formatter(string_rules)
    
    list_bibs_error = []
    for bibitem in filtered_publications:
        md_format = ''

        if 'author' not in global_index[bibitem].entry or 'title' not in global_index[bibitem].entry:
            # It skips bibitems with absence of authors or title
            continue

        for attr_key in global_index[bibitem].entry:
            global_index[bibitem].entry[attr_key] = global_index[bibitem].entry[attr_key].replace('{', '').replace('}', '')
        authors_format = bibtexformatter.authors_to_string(global_index[bibitem].author)
        title = codecs.decode(global_index[bibitem].entry['title'], "ulatex")
        md_format += 'title: ' + title + '\n'
        md_format += 'authors: ' + authors_format + '\n'
        
        pub_type = global_index[bibitem].entry_type
        if pub_type.lower() == '@phdthesis':
            md_format += 'template: publication-thesis\n'
            # TODO this is a hardcode capital first letter of bibkey
            md_format += 'coverpng: '+bibitem[0].title()+bibitem[1:]+'.png\n'
            for k in 'promotor', 'copromotor', 'school', 'optmonth', 'year':
                if k in global_index[bibitem].entry:
                    md_format += k+': ' + global_index[bibitem].entry[k] + '\n'
        else:
            md_format += 'template: publication\n'
            if 'booktitle' in global_index[bibitem].entry or 'journal' in global_index[bibitem].entry:
                event_type = 'journal' if 'journal' in global_index[bibitem].entry else 'booktitle'
                if global_index[bibitem].entry[event_type] in string_rules:
                    event_name = string_rules[global_index[bibitem].entry[event_type]]
                    event_name = event_name.replace('_', ' ').strip()
                else:
                    event_name = global_index[bibitem].entry[event_type]
                md_format += 'published_in: ' + event_name + '\n'
                _, pub_details = html_format.apply(global_index[bibitem])
                md_format += 'pub_details: ' + pub_details + '\n'
                    
            if 'doi' in global_index[bibitem].entry:
                md_format += 'doi: ' + 'https://doi.org/' + global_index[bibitem].entry['doi'] + '\n'
            if 'url' in global_index[bibitem].entry and 'arxiv' in global_index[bibitem].entry['url']:
                md_format += 'arxiv: ' + global_index[bibitem].entry['url'] + '\n'
            if 'pmid' in global_index[bibitem].entry:
                url_pmid = 'http://www.ncbi.nlm.nih.gov/pubmed/' + global_index[bibitem].entry['pmid']
                md_format += 'pmid: ' + url_pmid + '\n'
        if 'abstract' in global_index[bibitem].entry:
            md_format += global_index[bibitem].entry['abstract'] + '\n\n'

        # if 'file' in global_index[bibitem].entry:
        # TODO: Disabled for now as we don't have a version of the PDFs on the new website
        #     md_format += 'A <b>pdf file</b> of this publication is available for personal use.'
        #     md_format += 'Enter your e-mail address in the box below and press the button. '
        #     md_format += 'You will receive an e-mail message with a link to the pdf file.\n'
        #
        #     md_format += '<form action=\"sender.php\">'  # TODO implement sender.php
        #     md_format += '  <input type=\"text\" name=\"email\">'
        #     md_format += '  <input type=\"submit\" value=\"Send ' + global_index[bibitem].entry[
        #       'file'] + ' by e-mail\">'
        #     md_format += '</form>'

        md_format = md_format.replace('{', '').replace('}', '')
        out_path = os.path.join(out_dir, bibitem + '.md')

        file = open(out_path, 'w')

        try:  # This is ugly but necessary for now to avoid UnicodeEncodeError
            file.write(md_format)
            file.close()
        except UnicodeEncodeError:
            list_bibs_error.append(bibitem)
    print('List of bibkeys returning UnicodeEncodeError')

    for bib in list_bibs_error:
        print(bib)


def get_list_people():
    base_dir = os.getcwd()
    people_dir = '{}/content/pages/members'.format(base_dir)
    print(people_dir, '##')
    list_researchers = []

    for people_md_path in glob.glob(people_dir+'/*.md'):
        bname = os.path.basename(people_md_path).replace('.md', '')
        full_name = bname.split('-')
        list_researchers.append(full_name)

    return list_researchers


if __name__ == '__main__':
    generate_md_bibitem()
