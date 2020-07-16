import os

"""

MD files

"""


def save_md_file(output_path, md_content):
    '''
    save md cont to output path
    '''
    file = open(output_path, 'w', encoding='utf-8')
    file.write(md_content)
    file.close()


def create_author_md_files(author_bib_keys, list_researchers):
    '''
    Creates md file for every author in: './content/pages/publications/' 
    '''
    for name, bib_keys in author_bib_keys.items():
        author_name = name.replace('_', ' ')
        groups = list_researchers[name][1]
        md_string = 'title: Publications of ' + \
            list_researchers[name][2] + '\n'
        md_string += 'template: publications-author\n'
        md_string += 'author: ' + name.lower() + '\n'
        md_string += 'author_name: ' + list_researchers[name][2] + '\n'
        md_string += 'groups: ' + ','.join(groups) + '\n'
        md_string += 'bibkeys: ' + ','.join(bib_keys) + '\n'

        # standard
        standard_md_string = md_string + 'show_publication_years: ' + list_researchers[name][3]
        md_file_name = './content/pages/publications/' + name.lower() + '.md'
        save_md_file(md_file_name, standard_md_string)

        # all 
        all_md_string = md_string + 'show_publication_years: ' + 'no'
        dir_name = './content/pages/publications/' + name.lower()
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        save_md_file(os.path.join(dir_name, 'all.md'), all_md_string)


def create_publication_md(bib_items, author_bib_keys, list_researchers):
    '''
    Create md file for every publication in: './content/pages/publications/'
    '''
    for bib_key, bib_item in bib_items.items():
        diag_authors = []
        groups = set()
        for name, bib_keys in author_bib_keys.items():
            for bkey in bib_keys:
                if bib_key == bkey:
                    diag_authors.append(name)
                    for group in list_researchers[name][1]:
                        groups.add(group)

                    md_string = 'title: ' + bib_item['title'] + '\n'
                    md_string += 'authors: ' + bib_item['authors'] + '\n'
                    md_string += 'has_pdf: True \n' if 'file' in bib_item else 'has_pdf: False \n'
                    md_string += 'bibkey: ' + bib_key + '\n'
                    md_string += 'groups: ' + ','.join(groups) + '\n'
                    md_string += 'booktitle: NA \n' if 'booktitle' not in bib_item else 'booktitle: ' + \
                        bib_item['booktitle'] + '\n'
                    md_string += 'year: NA \n' if 'year' not in bib_item else 'year: ' + \
                        bib_item['year'] + '\n'
                    md_string += 'doi: NA \n' if 'doi' not in bib_item else 'doi: ' + \
                        bib_item['doi'] + '\n'

                    if bib_item['type'] == 'phdthesis':
                        md_string += 'template: publication-thesis\n'
                        # TODO this is a hardcode capital first letter of bibkey
                        cover_path = bib_key[0].title() + bib_key[1:] + '.png'
                        md_string += 'coverpng: ' + cover_path + '\n'
                        for k in 'promotor', 'copromotor', 'school', 'optmonth':
                            if k in bib_item:

                                md_string += k + ': ' + bib_item[k] + '\n'
                        if 'url' in bib_item:
                            md_string += 'urlweb: ' + bib_item['url'] + '\n'
                    else:
                        md_string += 'template: publication\n'
                        md_string += 'diag_authors: ' + \
                            ','.join(diag_authors) + '\n'
                        md_string += 'journal: NA \n' if 'journal' not in bib_item else 'journal: ' + \
                            bib_item['journal'] + '\n'

                    md_string += '' if 'abstract' not in bib_item else bib_item['abstract']
                    md_file_name = './content/pages/publications/' + bib_key + '.md'
                    save_md_file(md_file_name, md_string)
