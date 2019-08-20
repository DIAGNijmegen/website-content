"""
This plugins injects member information in to the generator.
"""

import os
import glob
from pelican import signals

member_tags = ['name', 'position', 'groups', 'picture', 'default_group']

def parse_member_file(file):
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
        data['default_group'] = data['groups'][0]

    return data

def load_member_data(generator):
    """Load all member data from the content dir"""

    files = glob.glob(os.path.join(os.getcwd(), '../content/pages/members/*.md'))

    member_data = {}

    for file in files:
        member = os.path.splitext(os.path.basename(file))[0]

        with open(file) as f:
            data = parse_member_file(f)
            member_data[data['name']] = data

    print(member_data)

    generator.context['members'] = member_data


def register():
    signals.generator_init.connect(load_member_data)
