import os

"""

MD files

"""

diag_bib = ['diag', 'pathology']
cara_bib = ['cara-lab']

def save_md_file(output_path, md_content):
    '''
    save md cont to output path
    '''
    file = open(output_path, 'w', encoding='utf-8')
    file.write(md_content)
    file.close()


def create_group_md_files(_bib_items, bib_items_per_group_per_date, rest_year=2012):
    for group, bib_items_per_date in bib_items_per_group_per_date.items():
        all_bib_items = []
        rest_bib_items = []
        md_content = {}
        md_content['main_title'] = 'main_title: Publications'
        md_content['template'] = 'template: publications'
        
        dir_name = os.path.join(f'./website-{group}/content/pages/publications/')
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)

        # per year
        for year, bib_items in bib_items_per_date.items():
            if not isinstance(year, int):
                continue
            all_bib_items.extend(bib_items)
            if int(year) <= rest_year:
                rest_bib_items.extend(bib_items)
            else:
                md_content['title'] = f'title: {year}'
                md_file_name = os.path.join(f'./website-{group}/content/pages/publications/{year}.md')
                save_md_file(md_file_name, '\n'.join(md_content.values()))


        if not os.path.isfile(f'./website-{group}/content/pages/publications.md'):
            # rest
            md_content['title'] = f'title: {rest_year} and before'
            md_file_name = os.path.join(f'./website-{group}/content/pages/publications/{rest_year}-and-before.md')
            save_md_file(md_file_name, '\n'.join(md_content.values()))

             # all 
            md_content['title'] = 'title: Publications'
            md_file_name = os.path.join(f'./website-{group}/content/pages/publications.md')
            save_md_file(md_file_name, '\n'.join(md_content.values()))
            
            md_content['title'] = 'title: All Years'
            md_file_name = os.path.join(f'./website-{group}/content/pages/publications/all-years.md')
            save_md_file(md_file_name, '\n'.join(md_content.values()))

            md_content['title'] = 'title: Most cited'
            gs_bib_items = [item for item in all_bib_items if 'gscites' in _bib_items[item]]
            gs_bib_items = sorted(gs_bib_items, key = lambda i: int(_bib_items[i]['gscites']),reverse=True) 
            md_content['bibkeys'] = f"bibkeys: {','.join(gs_bib_items[:100])}"
            md_file_name = os.path.join(f'./website-{group}/content/pages/publications/most-cited.md')
            save_md_file(md_file_name, '\n'.join(md_content.values()))
    

def create_author_md_files(bibfile, bib_items_per_author_per_date, list_researchers, rest_year=2012):
    '''
    Creates md file for every author in: './content/pages/publications/' 
    '''
    for name, bib_keys_per_date in bib_items_per_author_per_date.items():
        
        all_bib_keys = []
        rest_bib_keys = []
        md_content = {}
        md_content['main_title'] = 'main_title: Publications of ' + list_researchers[name][3]
        md_content['template'] = 'template: publications-author'
        md_content['author'] = 'author: ' + name.lower()
        md_content['author_name'] = 'author_name: ' + list_researchers[name][3]
        groups = list_researchers[name][1]
        md_content['groups'] = 'groups: ' + ','.join(groups)
 
        for group in groups:
            if (group == 'cara-lab' and bibfile == 'cara') or (group != 'cara-lab' and bibfile == 'diag'):
                dir_name = os.path.join(f'./website-{group}/content/pages/publications/',  name.lower())
                print(dir_name)
                if not os.path.exists(dir_name):
                    os.makedirs(dir_name, exist_ok=True)

                for year, bib_keys in bib_keys_per_date.items():
                    
                    if not isinstance(year, int):
                        continue
                    all_bib_keys.extend(bib_keys)
                    if int(year) <= rest_year:
                        rest_bib_keys.extend(bib_keys)
                    else:
                        # save publications of author per year
                        md_content['title'] = f'title: {str(year)}'
                        md_file_name = os.path.join(dir_name, str(year) + '.md')
                        save_md_file(md_file_name, '\n'.join(md_content.values()))
                    
                if rest_bib_keys:
                    md_content['title'] =f'title: {rest_year} and before'
                    md_file_name = os.path.join(dir_name, f'{rest_year}-and-before.md')
                    save_md_file(md_file_name, '\n'.join(md_content.values()))
                
                md_content['title'] = 'title: Publications of ' + list_researchers[name][3]
                md_file_name = dir_name + '.md'
                save_md_file(md_file_name, '\n'.join(md_content.values()))
                
                md_content['title'] = 'title: All Years'
                md_file_name = os.path.join(dir_name, 'all-years.md')
                save_md_file(md_file_name, '\n'.join(md_content.values()))

        # save_md_file(md_file_name, standard_md_string)

        # # no year heading
        # all_md_string = md_string + 'show_year_headings: ' + 'no'

        # save_md_file(os.path.join(dir_name, 'all.md'), all_md_string)

        # per year

def create_publication_md(bibfile, bib_items, bib_items_per_author_per_date, list_researchers):
    '''
    Create md file for every publication in: './content/pages/publications/'
    Now creates files for ALL publications, not just those with member authors
    '''
    for bib_key, bib_item in bib_items.items():

        diag_authors = []
        groups = set()

        # Check if this publication has any member authors
        has_member_author = False
        for name, bib_keys_per_date in bib_items_per_author_per_date.items():
            for year, bib_keys in bib_keys_per_date.items():
                if isinstance(year, int) and bib_key in bib_keys:
                    has_member_author = True
                    diag_authors.append(name)
                    for group in list_researchers[name][1]:
                        if (group == 'cara-lab' and bibfile == 'cara') or (group != 'cara-lab' and bibfile == 'diag'):
                            groups.add(group)

        # If no member authors found, assign to default groups based on bibfile
        if not groups:
            if bibfile == 'cara':
                groups.add('cara-lab')
            else:
                # For diag bibfile, add to relevant groups
                groups.update(['diag', 'pathology', 'anes'])

        # Create markdown string for publication
        md_string = 'title: ' + bib_item['title'] + '\n'
        md_string += 'authors: ' + bib_item['authors'] + '\n'
        md_string += 'has_pdf: True \n' if 'file' in bib_item else 'has_pdf: False \n'
        md_string += 'bibkey: ' + bib_key + '\n'
        md_string += 'groups: ' + ','.join(groups) + '\n'
        md_string += 'booktitle: NA \n' if 'booktitle' not in bib_item else 'booktitle: ' + \
            bib_item['booktitle'] + '\n'
        md_string += 'year: NA \n' if 'year' not in bib_item else 'year: ' + \
            str(bib_item['year']) + '\n'
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
