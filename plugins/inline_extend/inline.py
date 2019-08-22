import os
import re

from pelican import signals

# Group base urls
group_websites = {
    'diag': 'https://beta.diagnijmegen.nl',
    'pathology': 'https://www.computationalpathologygroup.eu',
    'retina': 'https://www.a-eyeresearch.nl',
    'rse': 'https://rse.diagnijmegen.nl',
    'bodyct': 'https://bodyct.diagnijmegen.nl',
    'aiimnijmegen': 'https://www.aiimnijmegen.nl',
    'rtc': 'https://diagnijmegen.github.io/website-msc-projects/',
    'neuro': 'https://diagnijmegen.github.io/website-neuro/',
    'diag': 'https://beta.diagnijmegen.nl'
}

# Matches: [member: Wouter Bulten, group: diag]
# group is optional
regex_member = re.compile(r"\[member:\s*(?P<member>[a-zA-Z\s]+)\s*(,\s*group: (?P<group>[a-zA-Z]+))?\]")

# Matches: [youtube: video_id]
regex_youtube = re.compile(r"\[youtube:\s*(?P<video>[a-zA-Z0-9\-\_]+)\]")
# Matches: [vimeo: video_id]
regex_vimeo = re.compile(r"\[vimeo:\s*(?P<video>[a-zA-Z0-9\-\_]+)\]")


def parse_member_tag(text, member_data):
    """Replaces [member: <name>] tags"""
    name = text.group('member')
    group = text.group('group')

    if name in member_data:
        url = member_data[name]['url']

        if group and group in group_websites:
            return f'<a href="{group_websites[group]}/members/{url}">{name}</a>'
        else:
            return f'<a href="{url}">{name}</a>'
    else:
        # For unknown members, just return the name
        print(f"Member {name} could not be found, no internal link generated.")
        return name

def parse_youtube_tag(text):
    """Replaces [youtube: id] tags"""
    video_id = text.group('video')

    return f'<div class="video-container"><iframe src="https://www.youtube-nocookie.com/embed/{video_id}" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe></div>'

def parse_vimeo_tag(text):
    """Replaces [vimeo: id] tags"""
    video_id = text.group('video')

    return f'<div class="video-container"><iframe src="https://player.vimeo.com/video/{video_id}" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe></div>'

def get_settings(generator):
    print(generator.context['MEMBER_DATA'])

def parse_tags(instance):
    """Function loops through all the pages and searches for tags"""

    if instance._content is not None:
        content = instance._content

        if '[member:' in content:
            content = regex_member.sub(lambda m: parse_member_tag(m, instance._context['MEMBER_DATA']), content)

        if '[youtube:' in content:
            content = regex_youtube.sub(lambda m: parse_youtube_tag(m), content)
        if '[vimeo:' in content:
            content = regex_vimeo.sub(lambda m: parse_vimeo_tag(m), content)

        instance._content = content
def register():
    #signals.generator_init.connect(get_settings)
    signals.content_object_init.connect(parse_tags)
