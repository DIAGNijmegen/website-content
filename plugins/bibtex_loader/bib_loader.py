"""
This plugin writes the md files for each publication found in bib_file (diag.bib by default)
It writes the output in 'out_dir'

@author Gabriel (ghumpire)
"""
import os
import json
from pelican import signals


def load_json2dict(json_path):
    if os.path.exists(json_path):
        json_file = open(json_path)
        json_data = json.load(json_file)
    else:
        json_data = {}

    return json_data
    

def load_bibkeys(generator):

    bibitems = load_json2dict('./content/bibitems.json')
    author_keys = load_json2dict('./content/authorkeys.json')

    generator.context['BIB_ITEMS'] = bibitems
    generator.context['AUTHOR_KEYS'] = author_keys 

def register():
    signals.generator_init.connect(load_bibkeys)
