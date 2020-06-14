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
    'rtc': 'https://rtc.diagnijmegen.nl',
    'neuro': 'https://diagnijmegen.github.io/website-neuro/',
    'diag': 'https://beta.diagnijmegen.nl'
}

# Matches: [member: Wouter Bulten, group: diag]
# group is optional
regex_member = re.compile(r"\[(?P<type>member|project|software|highlight|presentation|vacancy)\/(?P<identifier>[a-zA-Z-]+)\s*(,\s*group: (?P<group>[a-zA-Z]+))?\]")

# Matches: [youtube: video_id]
regex_youtube = re.compile(r"\[youtube:\s*(?P<video>[a-zA-Z0-9\-\_]+)\]")

# Matches: [vimeo: video_id]
regex_vimeo = re.compile(r"\[vimeo:\s*(?P<video>[a-zA-Z0-9\-\_]+)\]")

# Matches: [slideshare: slide_id]
regex_slideshare = re.compile(r"\[slideshare:\s*(?P<slide>[a-zA-Z0-9\-\_]+)\]")

# Matches: {{ IMGURL }}
regex_imgurl = re.compile(r"\{\{\s*IMGURL\s*\}\}")

# Content type to Pelican variable mapping
content_varnames = {
    'member': 'MEMBER_DATA',
    'project': 'PROJECT_DATA',
    'presentation': 'PRESENTATION_DATA',
    'highlight': 'HIGHLIGHT_DATA',
    'software': 'SOFTWARE_DATA',
    'vacancy': 'VACANCY_DATA',
}

def parse_content_tag(text, context):
    """Replaces tags that link to internal content  """
    identifier = text.group('identifier')
    group = text.group('group')
    type = text.group('type')

    # Retrieve data from the Pelican context
    data = context[content_varnames[type]]

    if identifier in data:
        # Detertime the label to show
        label = data[identifier]['name'] if 'name' in data[identifier] else data[identifier]['title']

        # Check if an explicit group is set, if so use that to build the link
        if group and group in group_websites:
            url = data[identifier]['url_internal']
            return f'<a href="{group_websites[group]}/{url}">{label}</a>'
        # If this page is part of the current website, create an internal link
        elif context['SITE_GROUP'] in data[identifier]['groups'] and context['SITE_GROUP'] in group_websites:
            url = data[identifier]['url_internal']
            return f'<a href="/{url}">{label}</a>'
        # If not group was set, and the page is not part of the current website, use the default url
        else:
            url = data[identifier]['url']
            return f'<a href="{url}">{label}</a>'
    else:
        # For unknown pages, just return the name
        print(f"Page {type}/{identifier} could not be found, no internal link generated.")
        return identifier

def parse_youtube_tag(text):
    """Replaces [youtube: id] tags"""
    video_id = text.group('video')
    return f'<div class="video-container"><iframe src="https://www.youtube-nocookie.com/embed/{video_id}" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe></div>'

def parse_vimeo_tag(text):
    """Replaces [vimeo: id] tags"""
    video_id = text.group('video')
    return f'<div class="video-container"><iframe src="https://player.vimeo.com/video/{video_id}" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe></div>'

def parse_slideshare_tag(text):
    slide_id = text.group('slide')
    return f'<div class="slide-container"><iframe src="https://www.slideshare.net/slideshow/embed_code/key/{slide_id}" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" allowfullscreen></iframe></div>'

def get_settings(generator):
    print(generator.context['MEMBER_DATA'])

def parse_tags(instance):
    """Function loops through all the pages and searches for tags"""

    if instance._content is not None:
        content = instance._content

        content = regex_member.sub(lambda m: parse_content_tag(m, instance._context), content)

        if '[youtube:' in content:
            content = regex_youtube.sub(lambda m: parse_youtube_tag(m), content)
        if '[vimeo:' in content:
            content = regex_vimeo.sub(lambda m: parse_vimeo_tag(m), content)
        if '[slideshare:' in content:
            content = regex_slideshare.sub(lambda m: parse_slideshare_tag(m), content)
        if 'IMGURL' in content:
            content = regex_imgurl.sub(lambda m: instance._context['IMGURL'], content)

        instance._content = content

def register():
    #signals.generator_init.connect(get_settings)
    signals.content_object_init.connect(parse_tags)
