"""
This plugin writes the md files for each publication found in bib_file (diag.bib by default)
It writes the output in 'out_dir'


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

    bibitems = load_json2dict('./content/bibitems_diag.json')
    author_keys = load_json2dict('./content/authorkeys_diag.json')
    group_keys = load_json2dict('./content/groupkeys_diag.json')

    bibitems_cara = load_json2dict('./content/bibitems_cara.json')
    author_keys_cara = load_json2dict('./content/authorkeys_cara.json')
    group_keys_cara = load_json2dict('./content/groupkeys_cara.json')

    if generator.context['SITE_GROUP'] != 'cara-lab':
        generator.context['BIB_ITEMS'] = bibitems
        generator.context['AUTHOR_KEYS'] = author_keys
        generator.context['GROUP_KEYS'] = group_keys
    else:
        generator.context['BIB_ITEMS'] = bibitems_cara
        generator.context['AUTHOR_KEYS'] = author_keys_cara
        generator.context['GROUP_KEYS'] = group_keys_cara

def register():
    signals.generator_init.connect(load_bibkeys)
