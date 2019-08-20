"""
This plugins injects member information in to the generator.
"""

import os
import glob
from pelican import signals

member_tags = ['name', 'position', 'groups', 'picture', 'default_group']

# Group base urls
group_websites = {
    'diag': 'https://beta.diagnijmegen.nl',
    'pathology': 'https://www.computationalpathologygroup.eu',
    'retina': 'https://www.a-eyeresearch.nl',
    'rse': 'https://rse.diagnijmegen.nl',
    'bodyct': 'https://bodyct.diagnijmegen.nl',
    'aiim': 'https://www.aiimnijmegen.nl',
    'rtc': 'https://diagnijmegen.github.io/website-msc-projects/',
    'neuro': 'https://diagnijmegen.github.io/website-neuro/',
    'diag': 'https://beta.diagnijmegen.nl'
}

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

    if data['default_group'] in group_websites:
        # Create link to profile page
        data['url'] = f"{group_websites[data['default_group']]}/members/{member}/"
    else:
        print(f"Could not set member url for member {member} as default group has no url ({data['default_group']}).")
        data['url'] = None

    return data

def load_member_data(generator):
    """Load all member data from the content dir"""

    files = glob.glob(os.path.join(os.getcwd(), '../content/pages/members/*.md'))

    member_data = {}

    for file in files:
        member = os.path.splitext(os.path.basename(file))[0]

        with open(file) as f:
            data = parse_member_file(member, f)
            member_data[data['name']] = data

    print(member_data)

    generator.context['MEMBER_DATA'] = member_data


def register():
    signals.generator_init.connect(load_member_data)
