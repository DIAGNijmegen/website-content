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
        json_data = None

    return json_data

    
def load_bibkeys(generator):
    json_path = generator.settings['BIBKEYS_SRC']
    bibkeys_html = load_json2dict(json_path)
    
    generator.context['bibkeys_html'] = bibkeys_html
    
    
def register():
    signals.generator_init.connect(load_bibkeys)
