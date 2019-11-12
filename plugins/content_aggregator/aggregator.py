"""
This plugins injects content information in to the generator.
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
for website in ['website-rtc', 'website-ai-for-health', 'website-diag', 'website-pathology', 'website-retina', 'website-bodyct', 'website-aiimnijmegen', 'website-neuro', 'website-rse']:
    DIAG_WEBSITES_NAMES[website[8:]] = importlib.import_module(f'{website}.pelicanconf').SITENAME
    DIAG_WEBSITE_URLS[website[8:]] = importlib.import_module(f'{website}.publishconf').SITEURL

# Dictionary that defines which content to read
# Format: <content type>: [list of tags to read]
content_types = {
    'member': {
        'dir': 'members',
        'url': 'members/{filename}/',
        'tags': ['name', 'position', 'groups', 'picture', 'default_group'],
        'varname': 'MEMBER_DATA',
    },
    'project': {
        'dir': 'projects',
        'url': 'projects/{filename}/',
        'tags': ['title', 'groups', 'picture', 'default_group'],
        'varname': 'PROJECT_DATA',
    },
    'presentation': {
        'dir': 'presentations',
        'url': 'presentations/{filename}/',
        'tags': ['title', 'groups', 'picture', 'default_group'],
        'varname': 'PRESENTATION_DATA',
    },
    'vacancy': {
        'dir': 'vacancies',
        'url': 'vacancies/{filename}/',
        'tags': ['title', 'groups', 'picture', 'default_group'],
        'varname': 'VACANCY_DATA',
    },
    'software': {
        'dir': 'software',
        'url': 'software/{filename}/',
        'tags': ['title', 'groups', 'picture', 'default_group'],
        'varname': 'SOFTWARE_DATA',
    },
    'highlight': {
        'dir': 'highlights',
        'url': 'highlights/{filename}/',
        'tags': ['title', 'groups', 'picture', 'default_group'],
        'varname': 'HIGHLIGHT_DATA',
    }
}

def parse_content_file(type, url, tags, content):
    """Parse a single member file"""
    data = {}
    for line in content:
        for tag in tags:
            if line.startswith(tag + ':'):
                value = line.split(':')[1].strip()

                # Expand lists
                if ',' in value:
                    data[tag] = value.split(',')
                else:
                    data[tag] = value

    if 'default_group' not in data and 'groups' in data:
        data['default_group'] = data['groups'][0] if isinstance(data['groups'], list) else data['groups']

    if type == 'member' and data['default_group'] == 'external':
        # Custom tag for member pages:
        # If the external tag is set, we need to favor the data in the external-people list.
        # The member is not included in the member-dictionary, this makes sure that the templates
        # get the data from the external people list.
        return None

    if data['default_group'] in DIAG_WEBSITE_URLS:
        # Create link to the page
        data['url'] = f"{DIAG_WEBSITE_URLS[data['default_group']]}/{url}"
        data['url_internal'] = url
        data['group_name'] = DIAG_WEBSITES_NAMES[data['default_group']]
    else:
        print(f"Could not set url for {type} page as default group has no url ({data['default_group']}).")
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

def load_content(generator):
    """Load content files from the content dir"""

    for type, config in content_types.items():

        files = glob.glob(os.path.join(os.getcwd(), f'../content/pages/{config["dir"]}/*.md'))
        aggregated_data = {}

        for file in files:

            # Create filename based on type and filename
            filename = os.path.splitext(os.path.basename(file))[0]

            with open(file, encoding="utf-8") as f:
                data = parse_content_file(
                    type=type,
                    url=config['url'].format(filename=filename),
                    tags=config['tags'],
                    content=f
                )

                if not data:
                    continue
                aggregated_data[filename] = data

        generator.context[config['varname']] = aggregated_data

    # Custom loader for external member data
    generator.context['EXTERNAL_PEOPLE_DATA'] = parse_external_member_data()

def register():
    signals.generator_init.connect(load_content)
