"""
This plugin monitor changes in content/diag.bib file
"""
from bibtex import bibtexlib
from bibtex import bibtexformatter
from pelican import signals
from pelican.readers import BaseReader


# Create BibReader class, inheriting from the pelican.reader.BaseReader
class BibReader(BaseReader):
    enabled = True
    # The list of file extensions you want this reader to match with.
    file_extensions = ['.bib']

    def read(self, filename):
        # This is needed only to monitor changes in bib files
        pass


def add_reader(readers):
    readers.reader_classes['.bib'] = BibReader


def register():
    signals.readers_init.connect(add_reader)


