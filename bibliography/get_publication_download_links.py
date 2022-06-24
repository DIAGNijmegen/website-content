import requests
# import lxml
from bs4 import BeautifulSoup
import unicodedata
import bibtexparser
from bibreader import parse_bibtex_file, get_bib_blocks
import latexcodec
import codecs
from difflib import SequenceMatcher
import time
import pandas as pd

def get_publication_page_url(bibkey, sleep_time=5):
    best_match_url = None
    best_match_title = None
    best_match_doi = None
    title_match_ratio = None
    search_string = None

    bib = diag_bib[bibkey]
    bib_title = bib['title'].strip()
    if 'doi' in bib:
        bib_doi = bib['doi']
    else:
        bib_doi = None
    bib_authors_name_string = ' '.join([name[2] for name in bib['author']])

    # SEARCH
    search_string = bib_title.strip() + ' ' + bib_authors_name_string
    search_string = search_string.replace(':', '')
    plus_search_string = search_string.replace(' ', '+')
    search_url = f'https://repository.ubn.ru.nl/discover?query={plus_search_string}&scope='
    time.sleep(sleep_time)
    additional_sleep_time = 10
    good_response = False
    while good_response == False:
        r_search = requests.get(search_url)
        if r_search.status_code == 429:
            time.sleep(additional_sleep_time)
            print(f'----429 response, slept for {additional_sleep_time} seconds (search request)')
            # sleep_time += 5
        else:
            good_response = True
    bs_search = BeautifulSoup(r_search.text, 'lxml')
    search_results = bs_search.find('div', id='aspect_discovery_SimpleSearch_div_search-results')

    # SEACH RESULTS
    results = search_results.find_all('div', class_='artifact-description')
    len_results = len(results)
    # If no results found
    if len_results == 0:
        return [bibkey, best_match_url,
                bib_title, bib_doi,
                best_match_title, best_match_doi,
                title_match_ratio, (bib_doi == best_match_doi) if bib_doi != None else False, search_string]

    # If results: find best title match
    ratios = []
    for result in results:
        match_title = result.a.h4.text.strip()
        a = bib_title.strip().lower()
        b = match_title.strip().lower()
        # TITLE RATIO
        title_match_ratio = SequenceMatcher(a=a, b=b).ratio()
        ratios.append(title_match_ratio)
    best_ratio_index = ratios.index(max(ratios))

    # try:
    if True:
        best_result = results[best_ratio_index]
        best_match_slug = best_result.a['href']
        best_match_title = best_result.a.h4.text.strip()
        a = bib_title.strip().lower()
        b = best_match_title.strip().lower()
        # TITLE RATIO
        title_match_ratio = SequenceMatcher(a=a, b=b).ratio()

        # First result page
        repo_url_base = "https://repository.ubn.ru.nl"
        best_match_url = repo_url_base + best_match_slug
        time.sleep(sleep_time)
        good_response = False
        while good_response == False:
            r_best_match = requests.get(best_match_url)
            if r_best_match.status_code == 429:
                time.sleep(additional_sleep_time)
                print(f'----429 response: slept for {additional_sleep_time} seconds (best match request) ')
                # sleep_time += 5
            else:
                good_response = True
        bs_best_match = BeautifulSoup(r_best_match.text, 'lxml')
        best_match_doi_div = bs_best_match.find('div', class_='simple-item-view-doi')
        # DOI
        if best_match_doi_div == None:
            best_match_doi = None
        else:
            best_match_doi = best_match_doi_div.a['href']
    # except Exception as e:
    #     print("--IN SEARCH LOOP--")
    #     print(bibkey, repr(e))
    #     exception = repr(e)

    # if title_match_ratio > 0.9 and bib_doi == best_match_doi:
    return [bibkey, best_match_url,
            bib_title, bib_doi,
            best_match_title, best_match_doi,
            title_match_ratio, (bib_doi == best_match_doi) if bib_doi != None else False, search_string]
    # else:
    #     return [bibkey, bib_title, bib_doi, None, title_match_ratio, best_match_doi]


# DOWNLOAD LATEST VERSION OF DIAG BIB AND FULLSTRINGS
download_bibs = True  # set to True if you want to download the diag.bib and fullstrings.bib

# DIAG BIB
diag_bib_raw_url = 'https://raw.githubusercontent.com/DIAGNijmegen/Literature/main/diag.bib'
r_diag_bib_raw = requests.get(diag_bib_raw_url).text
if download_bibs:
    with open("diag.bib", 'w', encoding="utf-8-sig") as file:
        file.write(r_diag_bib_raw)

# FULL STRINGS
fullstrings_raw_url = 'https://raw.githubusercontent.com/DIAGNijmegen/Literature/main/fullstrings.bib'
r_fullstrings_raw = requests.get(fullstrings_raw_url).text
if download_bibs:
    with open("fullstrings.bib", 'w', encoding="utf-8-sig") as file:
        file.write(r_fullstrings_raw)

# LOAD BIB FILES
diag_bib_path = 'diag.bib'  # r'C:\Users\joeyspronck\Downloads\diag.bib'
fullstrings_path = 'fullstrings.bib'  # r'C:\Users\joeyspronck\Downloads\fullstrings.bib'

diag_bib = parse_bibtex_file(diag_bib_path, fullstrings_path)

# LOAD BIBKEYS FOR WHICH WE NEED TO GET THE DOWNLOAD LINKS
with open('taverne_bibkeys.txt', 'r') as file:
    bibkeys = file.read().splitlines()


############ LOOP OVER ALL BIBKEYS ############

publication_page_urls = []
founds = []
not_found_in_bib = []
not_found_in_taverne = []
columns = ['bibkey', 'url',
           'bib_title', 'bib_doi',
           'match_title', 'match_doi',
           'title_match_ratio', 'same_doi', 'search_string']

for idx, bibkey in enumerate(bibkeys):
    if idx % 1 == 0:
        print(f'---[{idx}/{len(bibkeys)}]---')
    print(bibkey)

    if True:
    # try:
        publication_page_url = get_publication_page_url(bibkey.lower())
        [print(col+':', val) for col, val in zip(columns, publication_page_url)];
        print('\n')
    # except Exception as e:
    #     print('--IN BIBKEY LOOP--')
    #     print(bibkey, '  \t', repr(e))
    #     not_found_in_bib.append([bibkey, e])
    #     # publication_page_url = repr(e)
    #     continue

    publication_page_urls.append(publication_page_url)
print('DONE')

df = pd.DataFrame(publication_page_urls, columns=columns)
df.to_csv('publication_download_links.csv', index=False)
