
import os

from authors import  parse_name, split_authors, authors_to_string, get_list_researchers, get_publications_by_author


# pasre bib file
def get_bib_blocks(content, start_character='@', delim=('{','}')):
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
            if len(delimiter_stack)==0:
                start_index = content.rfind(start_character, 0, start)
                blocks.append((content[start_index: start], content[start + 1: i]))
    return blocks

def parse_bib_block_content(bib_item_text):
    '''
    Parses the a bib block 
    return the bib_key and the parsed bib_item
    '''
    bib_item = {}
    
    # split lines and remove ',' at the end
    bib_item_text = bib_item_text.replace('\r', '\n').replace('\r\n', '\n')
    lines  = bib_item_text.split(',\n')
    
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
 


def parse_bibtex_file(filename):
    '''
    Parse the bibtex file.
    return dictionary with bibkeys as keys and bib_items as values
    '''

    bib_items = {}
    string_rules = {}
    with open(filename, 'rb') as f:
        content = f.read().decode('utf-8-sig')

    for block in get_bib_blocks(content):
        block_name, block_content = block
        if block_name == '@Comment':
            continue
        elif block_name == '@String':
            k, v = [x.strip() for x in block_content.split('=')]
            string_rules[k] = v  
        else: #bib item text

            # parse bib item text
            bib_key, bib_item = parse_bib_block_content(block_content)
            
            # update type
            bib_item['type'] = block_name.strip('@').lower()
            
            # update journal name
            if 'journal' in bib_item:
                bib_item['journal'] = string_rules[bib_item['journal']].strip('_').replace('_', ' ') if bib_item['journal'] in string_rules else bib_item['journal']
                if 'arxiv' in bib_item['journal'].lower():
                    bib_item['type'] = 'preprint'

            if 'booktitle' in bib_item:
                bib_item['booktitle'] = string_rules[bib_item['booktitle']].strip('_').replace('_', ' ') if bib_item['booktitle'] in string_rules else bib_item['booktitle']

            if 'author' in bib_item:
                bib_item['author'] = list(map(parse_name, split_authors(bib_item['author'])))
                bib_item['authors'] = authors_to_string(bib_item['author'])

            if 'abstract' in bib_item:
                bib_item['abstract'] = bib_item['abstract'].replace('{', '').replace('}', '').replace('\\', '')
                
            if 'title' in bib_item:
                bib_item['title'] = bib_item['title'].replace('{', '').replace('}', '').replace('\\', '')
                bib_item['coverpng'] = bib_key[0].title() + bib_key[1:] + '.png'
                                                                                                      
            if 'copromotor' in bib_item:
                bib_item['author'] += list(map(parse_name, split_authors(bib_item['copromotor'])))
                bib_item['copromotor'] = authors_to_string(list(map(parse_name, split_authors(bib_item['copromotor']))))
           
            if 'promotor' in bib_item:
                bib_item['author'] += list(map(parse_name, split_authors(bib_item['promotor'])))
                bib_item['promotor'] = authors_to_string(list(map(parse_name, split_authors(bib_item['promotor']))))

            if 'pmid' in bib_item:
                bib_item['pmid'] = 'http://www.ncbi.nlm.nih.gov/pubmed/' + bib_item['pmid']
            
            if  'doi' in bib_item:
                bib_item['doi'] = 'https://doi.org/' + bib_item['doi']
            
            if 'url' in bib_item: 
                if 'arxiv' in bib_item['url']:
                    bib_item['url_type'] = 'ARXIV'
                else:
                    bib_item['url_type'] = 'URL'

            if 'year' not in bib_item:
                bib_item['year'] = '0000'

            cover_path = bib_key[0].title() + bib_key[1:] + '.png'
            bib_item['cover_exists'] = str(os.path.exists(os.path.join('.', 'content', 'images', 'theses', cover_path)))

            bib_items[bib_key.lower()] = bib_item
    return bib_items
