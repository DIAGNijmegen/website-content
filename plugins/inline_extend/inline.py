import os
import re

from pelican import signals

# Group base urls
group_websites = {
    'diag': 'https://www.diagnijmegen.nl',
    'pathology': 'https://www.computationalpathologygroup.eu',
    'retina': 'https://www.a-eyeresearch.nl',
    'rse': 'https://rse.diagnijmegen.nl',
    'rtc': 'https://rtc.diagnijmegen.nl',
    'diag': 'https://www.diagnijmegen.nl'
}

# Matches: [member/wouter-bulten, group: pathology]
# group is optional
regex_member = re.compile(r"\[(?P<type>member|project|software|highlight|presentation|vacancy)\/(?P<identifier>[a-zA-Z0-9-]+)\s*(,\s*group: (?P<group>[a-zA-Z]+))?\]")

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

        print(context['SITE_GROUP'])
        print(data[identifier]['url_groups'])
        
        # Check if an explicit group is set, if so use that to build the link
        if group and group in data[identifier]['url_groups']:
            url = data[identifier]['url_groups'][group]
            return f'<a href="{url}">{label}</a>'
        # If this page is part of the current website, create an internal link
        elif context['SITE_GROUP'] in data[identifier]['url_groups']:
            url = data[identifier]['url_groups'][context['SITE_GROUP']]
            return f'<a href="{url}">{label}</a>'
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

def parse_tags(content, context):
    """Function parses content and searches for tags to replace"""

    content = regex_member.sub(lambda m: parse_content_tag(m, context), content)

    if '[youtube:' in content:
        content = regex_youtube.sub(lambda m: parse_youtube_tag(m), content)
    if '[vimeo:' in content:
        content = regex_vimeo.sub(lambda m: parse_vimeo_tag(m), content)
    if '[slideshare:' in content:
        content = regex_slideshare.sub(lambda m: parse_slideshare_tag(m), content)
    if 'IMGURL' in content:
        content = regex_imgurl.sub(lambda m: context['IMGURL'], content)

    return content

def parse_content(instance):
    """Parse the content of a content object. This is done for every page."""
    if instance._content is not None:        
        instance._content = parse_tags(instance._content, instance._context)

def add_filter(pelican):
    """Add parse filter so that it can be used in places that are not part of the normal content object."""
    pelican.env.filters.update({'parse_custom_tags': lambda c: parse_tags(c, pelican.context)})

def register():
    """Plugin registration."""
    signals.generator_init.connect(add_filter)
    signals.content_object_init.connect(parse_content)
