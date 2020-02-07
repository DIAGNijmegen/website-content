import json
import time
import latexcodec
import codecs
import glob
import os 

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
            print('%r  %2.2f ms' % \
                  (method.__name__, (te - ts) * 1000))
        return result
    return timed


def authors_to_string(names, bib_key):
    string_authors = ''
    d = ', '
    for idx, name in enumerate(names):
        first, von, last, jr = name
        if first:
            first = first[0] + '.'
#         if first:
#             first = ''.join([f.strip('.').strip(',')[0].capitalize()+'.' for f in first.strip().replace('  ', ' ').split(' ')])
#         if '.' in von:
#             first = ''.join([first, *von.upper().split(' ')])
#             von = ''
#         if last:
#             last = '-'.join([l.capitalize() for l in last.strip().split('-')])
        if idx == len(names)-2:
            d = ' and '
        if idx == len(names)-1:
            d = ''
        string_authors += ' '.join(part for part in [first, von, last, jr] if part) + d
    return string_authors

# pasre bib file
def get_blocks(content, start_character='@', delim=('{','}')):
    '''
    returns all blocks (entries enclosed by the specified delimiters)
    start_character will look backwards from the start of the block for this character
    the result will be a tuple of two strings: from start character to start of the block, and the block content
    '''
    blocks = []
    
    delim_start, delim_end = delim
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

assert [x for x in get_blocks('abc = {test}, bac = {test2}', 'a')] == [('abc = ', 'test'), ('ac = ', 'test2')]


def decode_name(name):
    parsed_name = []
    for name_part in name:
        name_part = name_part.strip()
        if '\\' in name_part:
            name_part = codecs.decode(name_part, 'ulatex')
        parsed_name.append(name_part)
    return parsed_name


def parse_name(name):
    '''
    assumes this format:
    https://tex.stackexchange.com/questions/557/how-should-i-type-author-names-in-a-bib-file
    returns a tuple (first, von, last, jr)
    '''
    parts = name.strip(',').split(',')
    
    # "First von Last"
    if len(parts)==1:
        s, e = (name.index(' '), name.rfind(' ')) if ' ' in name else (0, 0)
        first = name[:s]
        von = name[s:e]
        last = name[e:]
        jr = ''
        
    # "von Last, First"
    elif len(parts)==2: 
        first = parts[1]
        e = parts[0].rfind(' ') if ' ' in parts[0] else 0
        von = parts[0][:e]
        last = parts[0][e:]
        jr = ''
        
    # "von Last, Jr, First"
    elif len(parts)==3: 
        first = parts[2]
        e = parts[0].rfind(' ') if ' ' in parts[0] else 0
        von = parts[0][:e]
        last = parts[0][e:]
        jr = parts[1]
        
    else:
        print('warning! bibtex format error in name "{}"'.format(''.join(name)))
        first, von, last, jr = '', '', name, ''  
    
    nfirst = ''
    for f in first.strip().split('.'):
        f = f.strip()
        f = f.capitalize()
        if len(f) == 1:
            f += '.'    
        nfirst = ' '.join([nfirst, f])
    
    #post process von to second names
    nvon = ''
    for v in von.strip().split():
        v = v.strip()
        if v[0].isupper():
            nfirst = ' '.join([nfirst, v])
        else:
            nvon = ' '.join([nvon, v])
    
    #post process first and second names
    nfirst2 = ''
    for f in nfirst.strip().split():
        f = f.strip()
        f = f.capitalize()
        if len(f) == 1:
            f += '.'    
        nfirst2 = ' '.join([nfirst2, f]) 
        
    last = '-'.join(last.strip().split())
        
    return decode_name((nfirst2, nvon, last, jr))


assert parse_name('Bart Liefers') == ['Bart', '', 'Liefers', '']
assert parse_name('Bart von Liefers') == ['Bart', 'von', 'Liefers', '']
assert parse_name('Liefers, Bart') == ['Bart', '', 'Liefers', '']
assert parse_name('von Liefers, Bart') == ['Bart', 'von', 'Liefers', '']
# assert parse_name('von Liefers, Jr, Bart') == ['Bart', 'von', 'Liefers', 'Jr']


def parse_block_content(bib_item_text):
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
 
def single_author(author_string):
    splits = author_string.split(',')
    splits = [s.strip() for s in splits]
    return len(splits) == 2 and not(' ' in splits[0] and ' ' in splits[1])

def split_authors(author_string):
    authors = []
    if 'and' in author_string.lower() or single_author(author_string):
        authors = author_string.replace('AND', 'and').split(' and ')
    else:
        authors = author_string.split(',')
    authors = [a.strip().replace('{', '').replace('}', '') for a in authors]
    return authors

def read_bibtex_file(filename):
    bib_items = {}
    string_rules = {}
    with open(filename, 'rb') as f:
        content = f.read().decode('utf-8-sig')

    for block in get_blocks(content):
        block_name, block_content = block
        if block_name == '@Comment':
            continue
        elif block_name == '@String':
            k, v = [x.strip() for x in block_content.split('=')]
            string_rules[k] = v  
        else: #bib item text

            # parse bib item text
            bib_key, bib_item = parse_block_content(block_content)
            
            # update type
            bib_item['type'] = block_name.strip('@').lower()
            
            # update journal name
            if 'journal' in bib_item:
                bib_item['journal'] = string_rules[bib_item['journal']].strip('_').replace('_', ' ') if bib_item['journal'] in string_rules else bib_item['journal']

            bib_item['author'] = list(map(parse_name, split_authors(bib_item['author'])))
            bib_item['authors'] = authors_to_string(bib_item['author'], bib_key)

            if 'abstract' in bib_item:
                bib_item['abstract'] = bib_item['abstract'].replace('{', '').replace('}', '').replace('\\', '').replace(':', '-')
                
            bib_item['title'] = bib_item['title'].replace('{', '').replace('}', '').replace('\\', '')

            if 'year' not in bib_item:
                bib_item['year'] = '0000'
                                                                                                      
            if 'copromotor' in bib_item:
                try:
                    bib_item['author'] += list(map(parse_name, split_authors(bib_item['copromotor'])))
                except:
                    print('bib_key cp', bib_key)
           
            if 'promotor' in bib_item:
                try:
                    bib_item['author'] += list(map(parse_name, split_authors(bib_item['promotor'])))
                except:
                    print('bib_key p', bib_key)
#             if 'optnote' in bib_item and 'diag' in bib_item['optnote'].lower():

            bib_items[bib_key.lower()] = bib_item
    return bib_items


# authors
def get_list_researchers(members_path):
    list_researchers = {}
    for people_md_path in glob.glob(members_path + '/*.md'):
        with open(people_md_path) as fp:
            # parse md file
            tags = {line.split(':')[0]:line.split(':')[1].strip().split() for line in (fp) if len(line.split(':')) > 1}

            # get publication name
            research_name = [n for n in tags['pub_name']] if 'pub_name' in tags else [n for n in tags['name']]
            name = '-'.join(tags['name'])
            groups =  [group.strip(',')  for group in tags['groups']]
        # append researches 
        list_researchers[name] = (research_name, groups)
    return list_researchers


# author publications
def get_publications_by_author(bib_items, list_researchers, debug_args=None):
    author_bibkeys = {}
    debug=False
    for bib_key, bib_item in bib_items.items():
        authors = bib_item['author']
        for name, value in list_researchers.items():
            researcher_name, groups = value
            firstname = researcher_name[0].lower()
            lastnames = [n.lower() for n in researcher_name[1:]]
            
            if debug_args:
                debug = True if bib_key == debug_args['bib_key'] and firstname == debug_args['firstname'] else False
                
            if len(lastnames) > 1:
                # This fixes issue #10 for lastnames connected with a dash (-)
                lastnames.append('-'.join(lastnames))
                
            for author_pub in authors:
                if match_author_publication(firstname, lastnames, author_pub, bib_key):
                    author_bibkeys.setdefault(name, []).append(bib_key)
    return author_bibkeys


def match_author_publication(firstname, lastnames, author, bib_key):
    # This function selects authors with the same lastname and matches the first name.
    # For instance, 'A. Patel' will always represent 'Ajay Patel' and not 'Anup Patel'.
    # If the bib file contains 'A Patel' then, it will associate the bibentry to 'Ajay Patel'.
    # If the bib file contains 'M F L Meijs' then, this script will not associate the bibentry to 'Midas Meijs'
    #  because it will check for the existence of von and jr (F and L in the example)
    author = [xname.replace('.', ' ').strip() for xname in author]
    try:
        first, von, last, jr = author
    except:
        print(author)
    first = first.lower()
    last = last.lower()
    jr = jr.lower()
    
    # Additional variable that may help to avoid incorrect name matching #77
    von_last = '-'.join([von, last])
    von_last = von_last.replace(' ', '-').lower()

    if last.lower() in lastnames:
        # First match based on last name
        if len(first) > 1 and first.lower() == firstname.lower() or len(jr) > 1 and jr.lower() in lastnames:
            # Easy match, the first name is complete and matches up
            return True
        elif len(first) > 1 and ' ' in first:
            # Incomplete match, some bib entries have authors as 'R Manniesing' instead of the full name
            # or 'J A W M van der Laak' where firstname contains 'J A W M'
            # or 'Jeroen AWM van der Laak' where firstname contains 'Jeroen A W M'
            # This piece of code makes sure there is only one name and no spaces in between
#             von = ' '.join(first.split(' ')[1:]) + ' ' + von
            first = first.split(' ')[0].lower()
            if first == firstname.lower():
                return True
            # if 'first' contains a single letter, it will continue

        if len(first) == 1 and first[0].lower() == firstname[0].lower():
            # If only one letter is provided as first name (incomplete in the bib entry).
            # An additional variable stores the initial lastnames
            initials_lastnames = [x[0].lower() for x in lastnames]
            if (len(von) == 0 and len(jr) == 0):
                # If there is no 'von' neither 'jr', then it is a match
                return True
            elif (len(jr) >= 1 and jr[0].lower() in initials_lastnames):
                # If 'jr' contains something, it will have to be listed on 'initials_lastnames'
                # to become a match
                return True
            elif (len(von.strip()) >= 1 and von.strip()[0].lower() in initials_lastnames):
                # If 'von' contains something, it will have to be listed on 'initials_lastnames'
                # to become a match
                return True
            elif '-' != von_last[0] and len(lastnames) >= 2 and lastnames[-1] in von_last:
                # If none of the previous methods worked, an additional checkup is done.
                # This is done only when having at least two last names.
                # the last lastname should be in 'von_last'.
                # For instance 'J A W M van der Laak' will become 'A-W-M-van-der-Laak', this matches up with 'van-der-laak'
                return True
        return False
    else:
        return False



"""

MD files

"""


def save_md_file(output_path, md_content):
    file = open(output_path, 'w', encoding='utf-8')
    file.write(md_content)
    file.close()
   
 
def create_author_md_files(author_bib_keys, list_researchers):
    for name, bib_keys in author_bib_keys.items():
        author_name = name.replace('_', ' ')
        groups = list_researchers[name][1]
        
        md_string = 'title: Publications of ' + author_name.replace('-', ' ') + '\n'
        md_string += 'template: publications-author\n'
        md_string += 'author: ' + name +'\n'
        md_string += 'author_name: ' + author_name.replace('-', ' ') + '\n'
        md_string += 'groups: ' + ','.join(groups) + '\n'
        md_string += 'bibkeys: ' + ','.join(bib_keys)
        md_file_name = './content/pages/publications/' +  name.lower() + '.md'
        save_md_file(md_file_name, md_string)
       
 
def create_publications_md(bib_items, author_bib_keys, list_researchers):
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
                    md_string += 'template: publication\n'
                    md_string += 'bibkey: ' + bib_key + '\n'
                    md_string += 'diag_authors: ' + ','.join(diag_authors) +'\n'
                    md_string += 'groups: ' + ','.join(groups) + '\n'
                    if 'journal' in bib_item:
                        md_string += 'published in: \n' if 'journal' not in bib_item else 'journal: ' + bib_item['journal'] + '\n'

                    if not 'journal' in bib_item and 'booktitle' in bib_item:
                        md_string += 'booktitle: ' + bib_item['booktitle'] +'\n'

                    md_string += 'pub_type: ' + bib_item['type'] +'\n' 
                    if 'year' in bib_item:
                        md_string += 'year: \n' if 'year' not in bib_item else 'year: ' + bib_item['year'] + '\n'
                    if 'doi' in bib_item:
                        md_string += 'doi: \n' if 'doi' not in bib_item else 'doi: ' + bib_item['doi'] + '\n'
                    if 'url' in bib_item:
                        md_string += 'url: \n' if 'url' not in bib_item else 'url: ' + bib_item['url'] + '\n'
                    md_string += 'authors: ' + bib_item['authors'] + '\n'
                    if 'abstract' in bib_item:
                        md_string += '' if 'abstract' not in bib_item else bib_item['abstract']
                    md_file_name = './content/pages/publications/' + bib_key + '.md'
                    save_md_file(md_file_name, md_string)


# get bib_items
@timeit
def run():
    bib_items = read_bibtex_file('./content/bib/diag.bib')
    list_researchers = get_list_researchers('./content/pages/members/')  
    author_bib_keys = get_publications_by_author(bib_items, list_researchers)
    save_dict2json('./content/bib/bibitems.json', bib_items)
    save_dict2json('./content/bib/authorkeys.json', author_bib_keys)
    return bib_items, list_researchers, author_bib_keys


if __name__ == "__main__":
    bib_items, list_researchers, author_bib_keys = run()
    create_author_md_files(author_bib_keys, list_researchers)
    create_publications_md(bib_items, author_bib_keys, list_researchers)
    	
