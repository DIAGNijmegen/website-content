#requires: pip install latexcodec
import latexcodec
from collections import defaultdict

# helper functions:

def get_blocks(content, start_character, delim=('{','}')):
    '''
    yields all blocks (entries enclosed by the specified delimiters)
    start_character will look backwards from the start of the block for this character
    the result will be a tuple of two strings: from start character to start of the block, and the block content
    '''
    delim_start, delim_end = delim
    stack = []
    for i, c in enumerate(content):
        if c == '{':
            stack.append(i)
        elif c == '}' and stack:
            start = stack.pop()
            if len(stack)==0:
                start_index = content.rfind(start_character, 0, start)
                yield content[start_index: start], content[start + 1: i]

assert [x for x in get_blocks('abc = {test}, bac = {test2}', 'a')] == [('abc = ', 'test'), ('ac = ', 'test2')]

def tokenize(string, delim=('{', '}'), trim=False):
    '''
    yields tokens instead of characters
    everything enclosed by the delimitors is returned as one token
    '''
    delim_start, delim_end = delim
    stack = []
    if trim:
        inp = string[1:-1]
    else:
        inp = string
    for i, c in enumerate(inp):
        if c == delim_start:
            stack.append(i)
        elif c == delim_end and stack:
            start = stack.pop()
            if len(stack) == 0:
                if trim:
                    yield(string[start+2:i+1])
                else:
                    yield(string[start:i+1])
            continue
        if len(stack) == 0:
            yield c

assert [x for x in tokenize('a{abc}c', delim=('{', '}'))] == ['a', '{abc}', 'c']
assert [x for x in tokenize('{a{abc}c{def}gh{i}}', delim=('{', '}'), trim=True)] == ['a', 'abc', 'c', 'def', 'g', 'h', 'i']

def list_split(lst, token):
    '''
    splits a list on a token
    yields individual parts of the list, split by the token
    '''
    last = -1
    for i, t in enumerate(lst):
        if t==token:
            yield lst[last+1:i]
            last = i
    yield lst[last+1:]

assert [x for x in list_split([1, 2, 3, 4], 2)]  == [[1], [3, 4]]

def token_split(token_list, pattern=' and '):
    '''
    splits a tokenlist on a pattern
    yields individual parts of the tokenlist, split by the pattern
    '''
    pattern_index = 0
    last = -1
    for i, t in enumerate(token_list):
        if t == pattern[pattern_index]:
            pattern_index += 1
            if pattern_index == len(pattern):
                yield token_list[last+1:i-len(pattern)+1]
                last = i
                pattern_index = 0
        else:
            pattern_index = 0
    yield token_list[last+1:]

assert [x for x in token_split([1, 2, 1, 'test', 2, 'test'], pattern = [1, 'test'])] == [[1, 2], [2, 'test']]

def rindex(lst, token):
    '''
    returns the last index of token in lst
    '''
    return next(i for i, v in zip(range(len(lst)-1, -1, -1), reversed(lst)) if v == token)

assert rindex('abc abc', 'a') == 4


def parse_name(name, omit=('{', '}')):
    '''
    assumes this format:
    https://tex.stackexchange.com/questions/557/how-should-i-type-author-names-in-a-bib-file
    cleans the string from characters in 'omit'

    returns a tuple (first, von, last, jr)
    '''
    parts = list(list_split(name, ','))
    if len(parts)==1:# "First von Last"
        if ' ' in name:
            s, e = name.index(' '), rindex(name, ' ')
        else:
            s, e = 0, 0
        first = name[:s]
        von = name[s:e]
        last = name[e:]
        jr = ''
    elif len(parts)==2: # "von Last, First"
        first = parts[1]
        e = rindex(parts[0], ' ') if ' ' in parts[0] else 0
        von = parts[0][:e]
        last = parts[0][e:]
        jr = ''
    elif len(parts)==3: # "von Last, Jr, First"
        first = parts[2]
        e = rindex(parts[0], ' ') if ' ' in parts[0] else 0
        von = parts[0][:e]
        last = parts[0][e:]
        jr = parts[1]
    else:
        print('warning! bibtex format error in name "{}"'.format(''.join(name)))
        first, von, last, jr = '', '', name, ''

    def clean(name_part):
        return ''.join(letter
                       for token in name_part
                       for letter in token
                       if not letter in omit).strip()
    return tuple(clean(x) for x in (first, von, last, jr))

assert parse_name('Bart Liefers') == ('Bart', '', 'Liefers', '')
assert parse_name('Bart von Liefers') == ('Bart', 'von', 'Liefers', '')
assert parse_name('Liefers, Bart') == ('Bart', '', 'Liefers', '')
assert parse_name('von Liefers, Bart') == ('Bart', 'von', 'Liefers', '')
assert parse_name('von Liefers, Jr, Bart') == ('Bart', 'von', 'Liefers', 'Jr')

def parse_authors(author_line):
    '''
    returns a list of author tuples
    '''
    author_line = author_line.replace('~', ' ')
    # remove enclosing braces
    try:
        cleaned_line = next(get_blocks(author_line, ''))[1]
    except:
        print('error in author line: {}'.format(author_line))
        cleaned_line = author_line[1:-1]


    #split on ' and ' tokens (but not between brackets!) to split out the separate authors
    authors = token_split(list(tokenize(cleaned_line)), pattern=' and ')
    return [parse_name(author) for author in authors]

assert parse_authors('{a and bandc and d { and } e}') == [('', '', 'a', ''), ('', '', 'bandc', ''), ('d', 'and', 'e', '')]

def get_entry_content(content):
    '''
    returns a dict mapping the bib-keys to
    '''
    def get_key_value(lines):
        for line in lines:
            if not '=' in line:
                continue
            i = line.index('=')
            key = line[:i].strip()
            value = line[i + 1:].strip()
            if value.startswith('{'):
                value = value[:rindex(value, '}') + 1]
            elif value.endswith(','):
                value = value[:-1]
            yield key, value
    return  {k: v for k, v in get_key_value(content.splitlines())}

def get_entry(entry):
    '''
    returns a tuple: the bibkey and a dict containing the key-values in this entry
    '''
    key_index = entry.index(',')
    bib_key = entry[:key_index]
    content = get_entry_content(entry[key_index:])
    return bib_key, content

def decode_latex(input_string, print_error_key=False):
    '''
        replace latex characters with unicode
    '''
    try:
        return input_string.encode('utf-8').decode('latex')
    except Exception as e:
        if print_error_key:
            print('{} : warning: encoding error!!!'.format(print_error_key))
            print(e)
        return input_string



def clean_bib_string(bib_string):
    if not bib_string[0] == '{' and bib_string[-1] == '}':
        print('unexpected content:', bib_string)
    return ''.join(b for b in tokenize(bib_string, trim=True))

class BibItem:

    url_syntax = {
        'doi': 'http://dx.doi.org/{}',
        'pmid': 'http://www.ncbi.nlm.nih.gov/pubmed/{}',
        'url': '{}'
    }

    def __init__(self, key, entry, entry_type):
        self.key = key
        self.entry = entry
        self.entry_type = entry_type
        self.values = {}

    def __getattr__ (self, key):
        if key in self.values:
            # memoization
            return self.values[key]

        if key == 'author':
            result = self._get_authors()
        elif key in ('journal', 'booktitle', 'title', 'series'):
            result = self._get_string_rule_or_decode(key)
        elif key in ('year', 'volume', 'pages', 'number'):
            result = self._get_simple_value(key).replace('--', '-')
        elif key in ('doi', 'pmid', 'url'):
            result = self._get_url(key)
        else:
            result = ''
        self.values[key] = result
        return result

    def _get_authors(self):
        if 'author' not in self.entry:
            return []
        return parse_authors(decode_latex(self.entry['author']))

    def _get_string_rule_or_decode(self, item):
        if not item in self.entry:
            return ''
        result = self.entry[item]
        if result.startswith('{'):
            return clean_bib_string(decode_latex(result))
        else:
            return result

    def _get_simple_value(self, key):
        if not key in self.entry:
            return ''
        else:
            value = self.entry[key]
            if value.startswith('{'):
                return value[1:-1]
            else:
                return value

    def _get_url(self, key):
        url = self._get_simple_value(key)
        if len(url):
            return self.url_syntax[key].format(url)
        return ''

### import and indexing
def read_bibtex_file(filename):
    index = defaultdict(dict)
    global_index = {}
    string_rules = {}
    with open(filename, 'rb') as f:
        content = f.read().decode('utf-8-sig')

    for type_name, entry in get_blocks(content, start_character='@'):
        if type_name == '@Comment':
            continue
        elif type_name == '@String':
            k, v = [x.strip() for x in entry.split('=')]
            string_rules[k] = v
        else:
            key, entry_dict = get_entry(entry)
            key = key.lower()
            bib_item = BibItem(key, entry_dict, type_name)
            global_index[key] = bib_item
            index[type_name][key] = bib_item

    return index, global_index, string_rules
