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

# Sites can save their profile pages using different patterns so we need to collect these
MEMBER_FILE_PATTERN = {}

for website in ['website-anes-ai']:
    
    website_config = importlib.import_module(f'{website}.pelicanconf')
    publish_config = importlib.import_module(f'{website}.publishconf')
    identifier = website[8:]

    DIAG_WEBSITES_NAMES[identifier] = website_config.SITENAME
    DIAG_WEBSITE_URLS[identifier] = publish_config.SITEURL
    MEMBER_FILE_PATTERN[identifier] = website_config.PAGE_MEMBERS_URL if hasattr(website_config, 'PAGE_MEMBERS_URL') else 'members/{slug}/'

# Dictionary that defines which content to read
# Format: <content type>: [list of tags to read]
CONTENT_TYPES = {
    'member': {
        'dir': 'members',
        'url': 'members/{slug}/',
        'tags': ['name', 'position', 'groups', 'email', 'picture', 'default_group'],
        'varname': 'MEMBER_DATA',
    },
    'project': {
        'dir': 'projects',
        'url': 'projects/{slug}/',
        'tags': ['title', 'groups', 'picture', 'default_group'],
        'varname': 'PROJECT_DATA',
    },
    'presentation': {
        'dir': 'presentations',
        'url': 'presentations/{slug}/',
        'tags': ['title', 'groups', 'picture', 'default_group'],
        'varname': 'PRESENTATION_DATA',
    },
    'vacancy': {
        'dir': 'vacancies',
        'url': 'vacancies/{slug}/',
        'tags': ['title', 'groups', 'picture', 'default_group'],
        'varname': 'VACANCY_DATA',
    },
    'software': {
        'dir': 'software',
        'url': 'software/{slug}/',
        'tags': ['title', 'groups', 'picture', 'default_group'],
        'varname': 'SOFTWARE_DATA',
    },
    'highlight': {
        'dir': 'highlights',
        'url': 'news/{slug}/',
        'tags': ['title', 'groups', 'picture', 'default_group'],
        'varname': 'HIGHLIGHT_DATA',
    }
}

def parse_content_file(type, filename, tags, content):
    """Parse a single member file"""
    data = {}
    for line in content:
        for tag in tags:
            if line.startswith(tag + ':'):
                value = line.split(':')[1].strip()

                # Expand lists
                if ',' in value:
                    data[tag] = [x.strip() for x in value.split(',')] # Remove whitespace in list
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

        # Create the absolute links for every site this page belongs to.
        data['url_groups'] = {}
        for group in data['groups'] if isinstance(data['groups'], list) else [data['groups']]:
            if group not in DIAG_WEBSITE_URLS:
                print(f"Skipping the creation of an url for group {group} and page {filename} as the group is invalid.")
                continue

            # For member pages we have to perform a rewrite of the url structure based on the site settings.
            # The absolute url is always based on the default group's settings.
            if type == 'member':
                url = MEMBER_FILE_PATTERN[group].format(slug=filename)
            else:
                url = CONTENT_TYPES[type]['url'].format(slug=filename)
            
            data['url_groups'][group] = f"{DIAG_WEBSITE_URLS[group]}/{url}"

        # Store the default absolute link to a page, always based on the default website's url.
        data['url'] = f"{data['url_groups'][data['default_group']]}"
        
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

    for type, config in CONTENT_TYPES.items():

        files = glob.glob(os.path.join(os.getcwd(), f'../content/pages/{config["dir"]}/*.md'))
        aggregated_data = {}

        for file in files:

            # Create filename based on type and filename
            filename = os.path.splitext(os.path.basename(file))[0]

            with open(file, encoding="utf-8") as f:
                data = parse_content_file(
                    type=type,
                    filename=filename,
                    tags=config['tags'],
                    content=f
                )

                if not data:
                    continue
                aggregated_data[filename] = data

        generator.context[config['varname']] = aggregated_data

        # For members we also need name-based matching
        if type == 'member':
            generator.context['MEMBER_DATA_PER_NAME'] = {x['name']: x for _, x in aggregated_data.items()}

    # Custom loader for external member data
    generator.context['EXTERNAL_PEOPLE_DATA'] = parse_external_member_data()

    # Set the links to all the diag websites
    generator.context['DIAG_WEBSITE_URLS'] = DIAG_WEBSITE_URLS
    generator.context['DIAG_WEBSITE_NAMES'] = DIAG_WEBSITES_NAMES 
    
def register():
    signals.generator_init.connect(load_content)
