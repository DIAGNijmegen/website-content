
import os

from authors import parse_name, split_authors, authors_to_string, get_list_researchers, get_publications_by_author
import codecs
import io

# pasre bib file
def get_bib_blocks(content, start_character='@', delim=('{', '}')):
    '''
    returns all bib blocks (entries enclosed by the specified delimiters)
    start_character will look backwards from the start of the block for this character
    the result will be a tuple of two strings: from start character to start of the block, and the block content
    '''
    blocks = []
    delimiter_stack = []
    for i, c in enumerate(content):
        if c == '{':
            delimiter_stack.append(i)
        elif c == '}' and delimiter_stack:
            start = delimiter_stack.pop()
            if len(delimiter_stack) == 0:
                start_index = content.rfind(start_character, 0, start)
                blocks.append(
                    (content[start_index: start], content[start + 1: i]))
    return blocks


def parse_bib_block_content(bib_item_text):
    '''
    Parses the a bib block 
    return the bib_key and the parsed bib_item
    '''
    bib_item = {}

    # split lines and remove ',' at the end
    bib_item_text = bib_item_text.replace('\r', '\n').replace('\r\n', '\n')
    lines = bib_item_text.split(',\n')

    # bib key
    bib_key = lines[0].lower()

    # parse lines
    for line in lines[1:]:

        # check if line is parseable
        if '=' not in line or line == '':
            continue

        # split by tags notated by '='
        key, value = line.split('=', 1)

        # strip unneccary symbols
        key = key.lower().strip()
        value = value.strip().strip('{').strip('}')

        # set bib_item
        bib_item[key] = value

    return bib_key, bib_item


def get_full_strings(full_strings_bib):
    string_rules = {}
    with open(full_strings_bib, 'rb') as f:
        content = f.read().decode('utf-8-sig')

    for block in get_bib_blocks(content):
        block_name, block_content = block
        if '@String' in block_name:
            k, v = [x.strip() for x in block_content.split('=')]
            string_rules[k.strip()] = v.strip()
    return string_rules

def get_arxiv_id_from_title(title):
    str_arxiv = title.lower().strip()
    id_arxiv = str_arxiv.replace('arxiv', '').replace(':', '').strip()
    url_arxiv = 'https://arxiv.org/abs/' + id_arxiv
    return url_arxiv

def parse_bibtex_file(filename, full_strings_bib):
    '''
    Parse the bibtex file.
    return dictionary with bibkeys as keys and bib_items as values
    '''

    full_strings_rules = get_full_strings(full_strings_bib)
    bib_items = {}
    string_rules = {}
    with open(filename, 'rb') as f:
        content = f.read().decode('utf-8-sig')

    for block in get_bib_blocks(content):
        block_name, block_content = block
        if '@comment' in block_name:
            continue
        elif '@string' in block_name:
            k, v = [x.strip() for x in block_content.split('=')]
            string_rules[k] = v
        else:  # bib item text

            # parse bib item text
            bib_key, bib_item = parse_bib_block_content(block_content)

            # update type
            bib_item['type'] = block_name.strip('@').lower()

            # update journal name
            if 'journal' in bib_item:
                name = bib_item['journal']
                if bib_item['journal'] in string_rules:
                    name = string_rules[bib_item['journal']]
                    if name in full_strings_rules:
                        name = full_strings_rules[name].strip('{').strip('}')
                    else:
                        name = name.replace('_', ' ').strip()
                elif name in full_strings_rules:
                    name = full_strings_rules[bib_item['journal']].strip(
                        '{').strip('}')

                bib_item['journal'] = codecs.decode(name, 'ulatex')

                if 'arxiv' in name.lower():
                    bib_item['type'] = 'preprint'
            if 'booktitle' in bib_item:
                name = bib_item['booktitle']
                if bib_item['booktitle'] in string_rules:
                    name = string_rules[bib_item['booktitle']]
                    if name in full_strings_rules:
                        name = full_strings_rules[name].strip('{').strip('}')
                    else:
                        name = name.replace('_', ' ').strip()
                elif bib_item['booktitle'] in full_strings_rules:
                    name = full_strings_rules[bib_item['booktitle']].strip(
                        '{').strip('}')

                bib_item['booktitle'] = codecs.decode(name, 'ulatex')

            if 'author' in bib_item:
                bib_item['author'] = list(
                    map(parse_name, split_authors(bib_item['author'])))
                bib_item['authors'] = authors_to_string(bib_item['author'])

            if 'abstract' in bib_item:
                abstract_temp = bib_item['abstract']
                bib_item['abstract'] = '\n\n'
                s = abstract_temp.replace('{', '').replace('}', '') 
                for s_ in s.split('\n'):
                    if len(s_.strip()) >0:
                        bib_item['abstract'] += s_.strip() + '\n\n'


            if 'title' in bib_item:
                bib_item['title'] = bib_item['title'].replace(
                    '{', '').replace('}', '').replace('\\', '')
                bib_item['coverpng'] = bib_key[0].title() + \
                    bib_key[1:] + '.png'

            if 'copromotor' in bib_item:
                bib_item['author'] += list(map(parse_name,
                                               split_authors(bib_item['copromotor'])))
                bib_item['copromotor'] = authors_to_string(
                    list(map(parse_name, split_authors(bib_item['copromotor']))))

            if 'promotor' in bib_item:
                bib_item['author'] += list(map(parse_name,
                                               split_authors(bib_item['promotor'])))
                bib_item['promotor'] = authors_to_string(
                    list(map(parse_name, split_authors(bib_item['promotor']))))

            if 'pmid' in bib_item:
                bib_item['pmid'] = 'http://www.ncbi.nlm.nih.gov/pubmed/' + \
                    bib_item['pmid']

            if 'doi' in bib_item:
                bib_item['doi'] = 'https://doi.org/' + bib_item['doi']

            if 'url' in bib_item:
                if 'arxiv' in bib_item['url']:
                    bib_item['url_type'] = 'arXiv'
                else:
                    bib_item['url_type'] = 'Url'
            elif bib_item['type'] == 'preprint':
                bib_item['url_type'] = 'arXiv'
                if bib_item['journal'] and 'arxiv' in bib_item['journal'].lower():
                    bib_item['url'] = get_arxiv_id_from_title(bib_item['journal'])

            if 'year' not in bib_item:
                print('no year found in bibitem. skipping bibitem:', bib_item)
                continue

            bib_item['pubinfo'] = bib_item['year'].strip()
            
            if 'volume' in bib_item:
                bib_item['pubinfo'] += ';' + bib_item['volume'].strip()

            if 'issue' in bib_item:
                bib_item['pubinfo'] += '(' + bib_item['issue'].strip() + ')'
                
            if 'pages' in bib_item:
                bib_item['pubinfo'] += ':' + bib_item['pages'].strip().replace('--', '-')

            cover_path = ''
            if len(bib_key) > 2:
                cover_path = bib_key[0].title() + bib_key[1:] + '.png'

            bib_item['cover_exists'] = str(os.path.exists(
                os.path.join('.', 'content', 'images', 'theses', cover_path)))

            bib_items[bib_key.lower()] = bib_item
    return bib_items
