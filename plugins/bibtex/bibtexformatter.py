import codecs
import latexcodec
from string import Formatter

def authors_to_string(authors):
    '''
    authors: list of author tuples
    '''
    def parse_author(author):
        first, von, last, jr = author
        
        if len(first)>=2 and first[1]=='.':
            # first probably contains initials
            initials = first
        else:
            initials = '.'.join(x[0] for x in first.split(' ') if x)
            if len(initials):
                initials += '.'
            
        result = initials        
        if not von == '':
            if len(von)>=2 and von[1]=='.':
                # von probably contains some initials
                result += von
            else:
                result += ' ' + von
        result += ' ' +last
        if not jr == '':
            result += ' ' + jr
        return result
    
    names = [parse_author(a) for a in authors]
    if len(names) == 1:
        return names[0]
    else:
        return ', '.join(names[:-1]) + ' and ' + names[-1] 


class BaseFormatter:
    
    def __init__(self, string_rules):
        self.string_rules = string_rules

    def apply_format(self, output, bib_item, **kwargs):
        def get_val(k):
            if k in kwargs:
                return kwargs[k]
            
            if not k in bib_item.entry:
                return ''
            
            value = getattr(bib_item, k)
            
            if k in ('journal', 'booktitle') and value in self.string_rules:
                return self.string_rules[value].replace('_', ' ').strip()
            else:
                return value
            
        field_names = [field_name for _, field_name, _, _ in Formatter().parse(output)]
        
        return output.format(**{k: get_val(k) for k in field_names})

    def format_proceedings(self):
        pass
    
    def format_abstract(self):
        pass
    
    def format_article(self):
        pass
    
    def format_thesis(self):
        pass
    
    def format_patent(self):
        pass
    
    def apply(self, bib_item):
        type_formatters = {
            '@InProceedings': self.format_proceedings,
            '@Conference': self.format_abstract,
            '@Article': self.format_article,
            '@PhdThesis': self.format_thesis,
            '@Mastersthesis': self.format_thesis,
            '@Patent': self.format_patent
        }
        if bib_item.entry_type in type_formatters:
            return type_formatters[bib_item.entry_type](bib_item)
        
class HTML_Formatter(BaseFormatter):
    
    def __init__(self, string_rules):
        super().__init__(string_rules)
        
    def format_proceedings(self, bib_item):
        authors = authors_to_string(bib_item.author)
        year_number_pages = ''
        
        # Gabriel: replaced for to handle attribute names before the value for instance 'i.e. pages 3'
        pub_tail = ''
        value_vol = getattr(bib_item, 'volume')
        value_ser = getattr(bib_item, 'series')
        if value_vol and value_ser: 
            pub_tail += ', volume {volume} of {series}'
        
        value = getattr(bib_item, 'year')
        if value:
            pub_tail += ', {year}'
        
        value = getattr(bib_item, 'number')
        if value:
            pub_tail += ', {number}'
        
        value = getattr(bib_item, 'pages')
        if value:
            pub_tail += ', pages {pages}'
        
        author_title = '{authors}. "{title}", '
        pub_details = 'in: <i>{booktitle}</i>' + pub_tail
        out_author_title = self.apply_format(author_title, bib_item, authors=authors)
        out_author_title = codecs.decode(out_author_title, "ulatex")
        out_pub_details = self.apply_format(pub_details, bib_item)
        # Gabriel: workaround to remove 'volume of , ' when volume is not present in bibitem
        output = out_author_title+out_pub_details
        
        return output, out_pub_details
        
    def format_abstract(self, bib_item):
        authors = authors_to_string(bib_item.author)
        author_title = '{authors}. "{title}", '
        pub_details = 'in: <i>{booktitle}</i>, {year}'
        out_author_title = self.apply_format(author_title, bib_item, authors=authors)
        out_author_title = codecs.decode(out_author_title, "ulatex")
        out_pub_details = self.apply_format(pub_details, bib_item)
        output = out_author_title+out_pub_details
        
        return output, out_pub_details

    def format_article(self, bib_item):
        authors = authors_to_string(bib_item.author)
        # TODO: The comment line of code was not working, it was printing always '{number}' in the parsed version. 
        # Gabriel replaced it by the current value, @Bart, please check if it is the corrrect way to do it.
        # nr = '({number})' if getattr(bib_item, 'number') else ''
        nr = '('+str(getattr(bib_item, 'number'))+')' if getattr(bib_item, 'number') else ''
        
        pub_tail = ';'
        value = getattr(bib_item, 'volume')
        if value:
            pub_tail += '{volume}{nr}'
        value = getattr(bib_item, 'pages')
        if value:
            pub_tail += ':{pages}' if len(pub_tail) > 1 else '{pages}'
        if len(pub_tail) == 1:
            # removing semicolon as the following attributes are absent: volume, nr, pages
            pub_tail = ''
        author_title = '{authors}. "{title}", '
        pub_details = '<i>{journal}</i> {year}' + pub_tail
        out_author_title = self.apply_format(author_title, bib_item, authors=authors)
        out_author_title = codecs.decode(out_author_title, "ulatex")
        out_pub_details = self.apply_format(pub_details, bib_item, nr=nr)
        output = out_author_title+out_pub_details
        
        return output, out_pub_details

    def format_thesis(self, bib_item):
        authors = authors_to_string(bib_item.author)
        
        if bib_item.entry_type == '@PhdThesis':
            name = '<i>PhD thesis</i>'
        elif bib_item.entry_type == '@Mastersthesis':
            name = '<i>Mastersthesis</i>'
        else:
            name = '?'
        school = getattr(bib_item, 'school')
        if school:
            school = ', {school}'
        author_title = authors +'. "{title}" '
        pub_details = name + school + ', {year}'
        out_author_title = self.apply_format(author_title, bib_item)
        out_author_title = codecs.decode(out_author_title, "ulatex")
        out_pub_details = self.apply_format(pub_details, bib_item)
        output = out_author_title+out_pub_details
        
        return output, out_pub_details


    def format_patent(self, bib_item):
        authors = authors_to_string(bib_item.author)
        author_title = '{authors}. "{title}" '
        pub_details = '{year}, {nationality}, patent number {optnumber}'
        out_author_title = self.apply_format(author_title, bib_item, authors=authors)
        out_author_title = codecs.decode(out_author_title, "ulatex")
        out_pub_details = self.apply_format(pub_details, bib_item)
        output = out_author_title+out_pub_details
        
        return output, out_pub_details
    
    
    