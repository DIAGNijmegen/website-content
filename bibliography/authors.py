import glob
import codecs

'''

This file contains author specific functions which are needed when parsing the bibfile.

'''


# authors
def get_list_researchers(members_path):
    '''
    Get all researched md files available in given member path 
    Checks if pub_name is availabe in md file and if true uses that as author name
    Extract groups from md file
    returns dictionary with name from md file as key, and tuple with (auhtor_name, groups) 
    '''
    list_researchers = {}
    for people_md_path in glob.glob(members_path + '/*.md'):
        # open md file
        with open(people_md_path) as fp:

            # get all tags and values in md file
            tags = {line.split(':')[0]: line.split(':')[1].strip(
            ).split() for line in (fp) if len(line.split(':')) > 1}

            # get author name, if pub_name in md file use that, else use name
            author_name = [n for n in tags['pub_name']
                           ] if 'pub_name' in tags else [n for n in tags['name']]

            # get name
            name = '-'.join(tags['name'])

            # get groups
            groups = [group.strip(',') for group in tags['groups']]

            # publication per year
            if 'show_publication_years' in tags:
                pub_per_year = tags['show_publication_years'][0]
            else:
                pub_per_year = 'yes'


        # append researcher with name as key and author_name and groups as value
        list_researchers[name.lower()] = (author_name, groups, name.replace('-', ' '), pub_per_year)
    return list_researchers


# author publications
def get_publications_by_author(bib_items, list_researchers):
    '''
    Get all publication per author
    returns dictionary with authorname as key and list of bib_keys as value
    '''
    author_bibkeys = {}
    for bib_key, bib_item in bib_items.items():
        if 'author' not in bib_item:
            continue
        authors = bib_item['author']
        for name, value in list_researchers.items():
            researcher_name, _, _, _ = value
            firstname = researcher_name[0].lower()
            lastnames = [n.lower() for n in researcher_name[1:]]

            if len(lastnames) > 1:
                # This fixes issue #10 for lastnames connected with a dash (-)
                lastnames.append('-'.join(lastnames))

            for author_pub in authors:
                if match_author_publication(firstname, lastnames, author_pub, bib_key):
                    author_bibkeys.setdefault(name.lower(), []).append(bib_key)
    return author_bibkeys


def match_author_publication(firstname, lastnames, author, bib_key):
    '''
    This function selects authors with the same lastname and matches the first name.
    For instance, 'A. Patel' will always represent 'Ajay Patel' and not 'Anup Patel'.
    If the bib file contains 'A Patel' then, it will associate the bibentry to 'Ajay Patel'.
    If the bib file contains 'M F L Meijs' then, this script will not associate the bibentry to 'Midas Meijs'
    because it will check for the existence of von and jr (F and L in the example)
    '''
    author = [xname.replace('.', ' ').strip() for xname in author]
    first, von, last, jr = author
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


def single_author(author_string):
    '''
    Checks if author is the single author
    '''
    splits = author_string.split(',')
    splits = [s.strip() for s in splits]
    return len(splits) == 2 and not(' ' in splits[0] and ' ' in splits[1])


def split_authors(author_string):
    '''
    Split all authors which are seperated by 'and' or ','
    returns all separeted authors
    '''
    authors = []
    if 'and' in author_string.lower() or single_author(author_string):
        authors = author_string.replace('AND', 'and').split(' and ')
    else:
        authors = author_string.split(',')
    authors = [a.strip() for a in authors]
    return authors


def decode_name(name):
    '''
    Decode name if backslash is in name
    '''
    parsed_name = []
    for name_part in name:
        name_part = name_part.strip()
        if '\\' in name_part:
            name_part = codecs.decode(name_part, 'ulatex')
        name_part = name_part.replace('{', '').replace('}', '')
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
    if len(parts) == 1:
        s, e = (name.index(' '), name.rfind(' ')) if ' ' in name else (0, 0)
        first = name[:s]
        von = name[s:e]
        last = name[e:]
        jr = ''

    # "von Last, First"
    elif len(parts) == 2:
        first = parts[1]
        e = parts[0].rfind(' ') if ' ' in parts[0] else 0
        von = parts[0][:e]
        last = parts[0][e:]
        jr = ''

    # "von Last, Jr, First"
    elif len(parts) == 3:
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


def authors_to_string(names):
    """
    creates a single string with all authors with only first letter of the firstname followed by a dot and surname. 
    Author names are sperated by comma except for the last author which is seperated via 'and'.
    """
    string_authors = ''
    d = ', '
    for idx, name in enumerate(names):
        first, von, last, jr = name
        if first:
            first = first[0] + '.'
        if idx == len(names)-2:
            d = ' and '
        if idx == len(names)-1:
            d = ''
        string_authors += ' '.join(
            part for part in [first, von, last, jr] if part) + d
    return string_authors
