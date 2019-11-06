"""
This plugins injects member information in to the generator.
"""

import os
import glob
import sys
import importlib
import yaml

from pelican import signals

# Load configs from all other websites
sys.path.insert(0, '../')
DIAG_WEBSITES_NAMES = {}
DIAG_WEBSITE_URLS = {}
for website in ['website-diag', 'website-pathology', 'website-retina', 'website-bodyct', 'website-aiimnijmegen', 'website-neuro', 'website-rse']:
    DIAG_WEBSITES_NAMES[website[8:]] = importlib.import_module(f'{website}.pelicanconf').SITENAME
    DIAG_WEBSITE_URLS[website[8:]] = importlib.import_module(f'{website}.publishconf').SITEURL

member_tags = ['name', 'position', 'groups', 'picture', 'default_group']

def parse_member_file(member, file):
    """Parse a single member file"""
    data = {}
    for line in file:
        for tag in member_tags:
            if line.startswith(tag + ':'):
                value = line.split(':')[1].strip()

                # Expand lists
                if ',' in value:
                    data[tag] = value.split(',')
                else:
                    data[tag] = value

    if 'default_group' not in data and 'groups' in data:
        data['default_group'] = data['groups'][0] if isinstance(data['groups'], list) else data['groups']

    if data['default_group'] == 'external':
        # If the external tag is set, we need to favor the data in the external-people list.
        # The member is not included in the member-dictionary, this makes sure that the templates
        # get the data from the external people list.
        return None

    if data['default_group'] in DIAG_WEBSITE_URLS:
        # Create link to profile page
        data['url'] = f"{DIAG_WEBSITE_URLS[data['default_group']]}/members/{member}/"
        data['group_name'] = DIAG_WEBSITES_NAMES[data['default_group']]
    else:
        print(f"Could not set member url for member {member} as default group has no url ({data['default_group']}).")
        data['url'] = None
        data['group_name'] = ''

    return data

def parse_external_member_data():
    """Load data from the external people data file"""
    file_location = os.path.join(os.getcwd(), '../content/external-people.yaml')

    data = {}

    with open(file_location, encoding="utf-8") as stream:
        raw_data = yaml.safe_load(stream)

        for person in raw_data['people']:
            data[person['name']] = person

    return data

def load_member_data(generator):
    """Load all member data from the content dir"""

    files = glob.glob(os.path.join(os.getcwd(), '../content/pages/members/*.md'))

    member_data = {}

    for file in files:
        member = os.path.splitext(os.path.basename(file))[0]

        with open(file, encoding="utf-8") as f:
            data = parse_member_file(member, f)
            if data:
                member_data[data['name']] = data



    generator.context['MEMBER_DATA'] = member_data
    generator.context['EXTERNAL_PEOPLE_DATA'] = parse_external_member_data()

def register():
    signals.generator_init.connect(load_member_data)
