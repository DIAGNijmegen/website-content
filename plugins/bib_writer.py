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
import traceback

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


class PublicationsGenerator:
    # Class PublicationsGenerator reads the diag.bib file to process it and generate the publications
    # list of researchers/members.
    #
    # The main function is generate_md_bibitem(), the remaining functions are private functions.
    # See the __main__ section to check how to run this python script.
    #
    # Algorithm:
    # 1. This python script uses bibtexlib (Bart designed it) to parse effitiently the large diag.bib file in
    #    a couple of seconds.
    # 2. We obtain the list of researchers/members/authors of the current website. This is done in __get_list_people().
    # 3. We filter out publications of the researchers/members/author of the current website. This is done in
    #    __get_publications_by_author().
    # 4. Generate markdown files per publication. This is done in __write_single_publication_md().
    #    Sample: Publication of bibkey balo18 https://www.computationalpathologygroup.eu/publications/balo18/
    # 5. The publications are grouped by author to create markdown files. This is done in __write_author_publications_md().
    #    Sample: List of publications of Francesco https://www.computationalpathologygroup.eu/publications/francesco-ciompi/
    # 6. The full list of publications are generated in __write_list_publications_md().
    #    Sample: Full list of publication of the pathology group https://www.computationalpathologygroup.eu/publications/
    # 7. Additional information is stored in content/dict_pubs.json as json file.
    #
    @staticmethod
    def __match_author_publication(firstname, lastnames, author):
        # This function selects authors with the same lastname and matches the first name.
        # For instance, 'A. Patel' will always represent 'Ajay Patel' and not 'Anup Patel'.
        # If the bib file contains 'A Patel' then, it will associate the bibentry to 'Ajay Patel'.
        # If the bib file contains 'M F L Meijs' then, this script will not associate the bibentry to 'Midas Meijs'
        #  because it will check for the existence of von and jr (F and L in the example)
        first, von, last, jr = author
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
                von = ' '.join(first.split(' ')[1:]) + ' ' + von
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
                elif (len(von) >=1 and von[0].lower() in initials_lastnames):
                    # If 'von' contains something, it will have to be listed on 'initials_lastnames'
                    # to become a match
                    return True
                elif '-' != von_last[0] and len(lastnames) >=2 and lastnames[-1] in von_last:
                    # If none of the previous methods worked, an additional checkup is done.
                    # This is done only when having at least two last names.
                    # the last lastname should be in 'von_last'.
                    # For instance 'J A W M van der Laak' will become 'A-W-M-van-der-Laak', this matches up with 'van-der-laak'
                    return True
            return False
        else:
            return False

    def __get_publications_by_author(self, global_index, list_researchers):
        from collections import defaultdict
        author_index = defaultdict(set)
        filtered_bibkeys = []

        for bib_key, bib_item in global_index.items():
            authors = bib_item.author

            for researcher_names in list_researchers:
                firstname = researcher_names[0]
                lastnames = researcher_names[1:]
                if len(lastnames) > 1:
                    # This fixes issue #10 for lastnames connected with a dash (-)
                    lastnames.append('-'.join(lastnames))
                lastnames = [lname.lower() for lname in lastnames]
                for author_pub in authors:
                    # Some bib entries are like 'R. Manniesing', the next line of code removes the '.'
                    author_pub = [xname.replace('.', '') for xname in author_pub]
                    try:
                        if self.__match_author_publication(firstname, lastnames, author_pub):
                            von = author_pub[1]
                            lastname = author_pub[2]
                            author_index[lastname.lower()].add(bib_key)
                            # Some 'von' are actually lastnames
                            pvon = von.replace(' ', '').replace('.', '')

                            if len(lastnames) > 1:
                                author_index[lastnames[-2]].add(bib_key)
                                author_index[lastnames[-1]].add(bib_key)
                            if len(pvon) > 3:
                                author_index[von].add(bib_key)
                            if bib_key not in filtered_bibkeys:
                                filtered_bibkeys.append(bib_key)
                    except Exception as exc:
                        # Failed to parse this bibentry, report it but don't kill the build
                        print(f"Failed parsing bibentry for {firstname} {' '.join(lastnames)} and bib key {bib_key}. This entry is skipped.")
                        print(traceback.format_exc())
        return author_index, filtered_bibkeys

    @staticmethod
    def __get_list_people():
        base_dir = os.getcwd()
        people_dir = '{}/content/pages/members'.format(base_dir)
        print(people_dir)
        list_researchers = []

        for people_md_path in glob.glob(people_dir + '/*.md'):
            bname = os.path.basename(people_md_path).replace('.md', '')
            full_name = bname.split('-')
            list_researchers.append(full_name)
            print('Member: ', full_name)

        return list_researchers

    @staticmethod
    def __get_arxiv_id_from_title(title):
        str_arxiv = title.lower().strip()
        id_arxiv = str_arxiv.replace('arxiv', '').replace(':', '').strip()
        url_arxiv = 'https://arxiv.org/abs/' + id_arxiv
        return url_arxiv

    @staticmethod
    def __write_md_pass(out_path, md_format):
        file = open(out_path, 'w', encoding='utf-8')

        try:  # This is ugly but necessary for now to avoid UnicodeEncodeError
            file.write(md_format)
            file.close()
        except UnicodeEncodeError:
            pass

    @staticmethod
    def __cleanup_global_index(global_index, bibkey):
        for attr_key in global_index[bibkey].entry:
            global_index[bibkey].entry[attr_key] = global_index[bibkey].entry[attr_key].replace('{', '')
            global_index[bibkey].entry[attr_key] = global_index[bibkey].entry[attr_key].replace('}', '')

        return global_index

    def generate_md_bibitem(self):
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

        # Parses diag.bib
        start_time = time.clock()
        index, global_index, string_rules = bibtexlib.read_bibtex_file(bib_file)
        time_diagbib = time.clock() - start_time
        start_time = time.clock()

        if not os.path.exists(out_dir):
            os.makedirs(out_dir)

        # Retrieves list of members and their publications
        list_researchers = self.__get_list_people()
        author_index, filtered_bibkeys = self.__get_publications_by_author(global_index, list_researchers)

        # Writes single md files per publication
        self.__write_single_publication_md(global_index, string_rules, filtered_bibkeys, out_dir)
        print('\nTime to process diag.bib ', time_diagbib)
        print('Time to create ' + str(len(global_index)) + ' MD files ', time.clock() - start_time)

        # Writes list of publications of a member
        time_list_pubs = time.clock()
        self.__write_author_publications_md(author_index, list_researchers, out_dir)
        dict_pubs = self.__write_list_publications_md(global_index, filtered_bibkeys, string_rules)
        print('Time to create filtered list of publications and publications per researcher',
              time.clock() - time_list_pubs)

        # Stores metadata as json file
        json_path = os.path.join(base_dir, '..', 'content/dict_pubs.json')
        save_dict2json(json_path, dict_pubs)

    def __write_list_publications_md(self, global_index, filtered_bibkeys, string_rules):
        html_format = bibtexformatter.HTML_Formatter(string_rules)

        dict_pubs = {}
        for bib_key in filtered_bibkeys:
            bib_key = bib_key.lower()
            try:
                html_bibkey, year, pub_type, pub_details = self.__append_publication_md(global_index, bib_key, html_format)
                pub_details = pub_details.replace('_', ' ').strip()
                dict_pubs[bib_key] = {}
                dict_pubs[bib_key]['html'] = html_bibkey
                dict_pubs[bib_key]['year'] = int(year)
                dict_pubs[bib_key]['pub_type'] = pub_type
                dict_pubs[bib_key]['pub_details'] = pub_details
                if pub_type.lower() == '@phdthesis':
                    dict_pubs[bib_key]['author_name'] = global_index[bib_key].entry['author']
                    dict_pubs[bib_key]['title_thesis'] = global_index[bib_key].entry['title']
                    # TODO this is a hardcode capital first letter of bibkey
                    dict_pubs[bib_key]['coverpng'] = bib_key[0].title() + bib_key[1:] + '.png'
            except:
                print(f"Failed writing html for publication list for {bib_key}, skipping this entry.")
                print(traceback.format_exc())
        return dict_pubs

    def __write_author_publications_md(self, author_index, list_researchers, out_dir):
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
            md_format += 'bibkeys: ' + ','.join(list_pubs_author)
            out_path = os.path.join(out_dir, full_name + '.md')
            self.__write_md_pass(out_path, md_format)

    def __write_single_publication_md(self, global_index, string_rules, filtered_bibkeys, out_dir):
        html_format = bibtexformatter.HTML_Formatter(string_rules)

        list_bibs_error = []
        for bibkey in filtered_bibkeys:
            try:
                md_format = ''

                if 'author' not in global_index[bibkey].entry or 'title' not in global_index[bibkey].entry:
                    # It skips bibkeys either without authors or title
                    continue

                global_index = self.__cleanup_global_index(global_index, bibkey)
                authors_format = bibtexformatter.authors_to_string(global_index[bibkey].author)
                title = codecs.decode(global_index[bibkey].entry['title'], "ulatex")
                md_format += 'title: ' + title + '\n'
                md_format += 'authors: ' + authors_format + '\n'
                pub_type = global_index[bibkey].entry_type
                has_pdf = 'file' in global_index[bibkey].entry
                md_format += 'has_pdf: ' + str(has_pdf) + '\n'
                if pub_type.lower() == '@phdthesis':
                    md_format += 'template: publication-thesis\n'
                    # TODO this is a hardcode capital first letter of bibkey
                    md_format += 'coverpng: ' + bibkey[0].title() + bibkey[1:] + '.png\n'
                    for k in 'promotor', 'copromotor', 'school', 'optmonth', 'year':
                        if k in global_index[bibkey].entry:
                            md_format += k + ': ' + global_index[bibkey].entry[k] + '\n'
                    if 'url' in global_index[bibkey].entry:
                        url_pub = global_index[bibkey].entry['url']
                        md_format += 'urlweb: ' + url_pub + '\n'
                else:
                    md_format += 'template: publication\n'
                    md_format += 'bibkey: ' + bibkey + '\n'
                    if 'booktitle' in global_index[bibkey].entry or 'journal' in global_index[bibkey].entry:
                        event_type = 'journal' if 'journal' in global_index[bibkey].entry else 'booktitle'
                        if global_index[bibkey].entry[event_type] in string_rules:
                            event_name = string_rules[global_index[bibkey].entry[event_type]]
                        else:
                            event_name = global_index[bibkey].entry[event_type]
                        event_name = event_name.replace('_', ' ').strip()
                        md_format += 'published_in: ' + event_name + '\n'
                        _, pub_details = html_format.apply(global_index[bibkey])
                        pub_details = pub_details.replace('_', ' ').strip()
                        md_format += 'pub_details: ' + pub_details + '\n'

                    md_format_bibitem, is_preprint = self.__format_bibitem(global_index[bibkey], is_html_format=False)
                    md_format += md_format_bibitem

                if 'abstract' in global_index[bibkey].entry:
                    md_format += global_index[bibkey].entry['abstract'] + '\n\n'

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
                out_path = os.path.join(out_dir, bibkey + '.md')

                file = open(out_path, 'w')

                try:  # This is ugly but necessary for now to avoid UnicodeEncodeError
                    file.write(md_format)
                    file.close()
                except UnicodeEncodeError:
                    list_bibs_error.append(bibkey)
            except Exception as exc:
                print(f"Failed writing bib entry {bibkey} to markdown file.")
                print(traceback.format_exc())

        print('List of bibkeys returning UnicodeEncodeError')
        for bib in list_bibs_error:
            print(bib)

    def __append_publication_md(self, global_index, bib_key, html_format):
        bib_item = global_index[bib_key]
        html_to_write, pub_details = html_format.apply(bib_item)
        html_to_write = html_to_write.replace('_', ' ').strip()
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

        html_format, new_pubtype = self.__format_bibitem(bib_item, is_html_format=True)
        pub_html += html_format

        if new_pubtype is not None:
            pub_type = new_pubtype
        pub_html += '</li>\n'

        return pub_html, year, pub_type, pub_details

    def __format_bibitem(self, bib_item, is_html_format=True):
        formatted_text = ''
        new_pubtype = None
        if 'doi' in bib_item.entry:
            url_doi = 'https://doi.org/' + bib_item.entry['doi']
            if is_html_format:
                formatted_text += ' <a href=\"' + url_doi + '\">DOI</a>'
            else:
                formatted_text += 'doi: ' + url_doi + '\n'
        if 'url' in bib_item.entry and 'arxiv' in bib_item.entry['url']:
            url_arxiv = bib_item.entry['url']
            if is_html_format:
                formatted_text += ' <a href=\"' + url_arxiv + '/\">arXiv</a>'
            else:
                formatted_text += 'arxiv: ' + url_arxiv + '\n'
        elif 'url' in bib_item.entry:
            url_pub = bib_item.entry['url']
            if is_html_format:
                formatted_text += ' <a href=\"' + url_pub + '/\">URL</a>'
            else:
                formatted_text += 'urlweb: ' + url_pub + '\n'
        if 'journal' in bib_item.entry and 'arxiv' in bib_item.entry['journal'].lower():
            # If an entry has arxiv as journal, then it is considered as @Preprint
            url_arxiv = self.__get_arxiv_id_from_title(bib_item.entry['journal'])
            if is_html_format:
                formatted_text += ' <a href=\"' + url_arxiv + '/\">arXiv</a>'
            else:
                formatted_text += 'arxiv: ' + url_arxiv + '\n'
            new_pubtype = '@Preprint'
        elif  bib_item.entry_type.lower() not in ['@inproceedings', '@conference', '@article', '@phdthesis', '@mastersthesis', '@patent', '@book']:
            # See the full list of publication types in bibtex/bibtexformatter.py (variable type_formatters)
            new_pubtype = '@Other'

        if 'pmid' in bib_item.entry:
            url_pmid = 'http://www.ncbi.nlm.nih.gov/pubmed/' + bib_item.entry['pmid']
            if is_html_format:
                formatted_text += ' <a href=\"' + url_pmid + '/\">PMID</a>'
            else:
                formatted_text += 'pmid: ' + url_pmid + '\n'

        return formatted_text, new_pubtype


if __name__ == '__main__':
    pubgen = PublicationsGenerator()
    pubgen.generate_md_bibitem()
