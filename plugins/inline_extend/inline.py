import os
import re

from pelican import signals

regex_member = re.compile('\[member: (?P<member>[a-zA-Z\s]+)\]')

def parse_member_tag(text):
    """Replaces [member: <name>] tags"""
    name = text.group('member')
    name_url = name.lower().replace(' ', '-')

    return f'<a href="/members/{name_url}">{name}</a>'

def get_settings(generator):
    print(generator.settings['SITEURL'])

def parse_tags(instance):
    """Function loops through all the pages and searches for tags"""

    if instance._content is not None:
        content = instance._content

        if '[member:' in content:
            content = regex_member.sub(lambda m: parse_member_tag(m), content)

        instance._content = content
def register():
    #signals.generator_init.connect(get_settings)
    signals.content_object_init.connect(parse_tags)
