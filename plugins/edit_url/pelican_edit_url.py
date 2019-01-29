"""
Edit URL
========
This plugin adds an edit_url property to content objects
that correspond to a place online to edit the content
(usually Github).
"""
import os.path

from pelican import signals


def add_edit_url(instance):
    EDIT_CONTENT_URL = instance.settings.get('EDIT_CONTENT_URL', None)
    WEBSITE = instance.settings.get('SITE_REPO', None)
    if EDIT_CONTENT_URL is None:
        return
    if WEBSITE is None:
        return

    # assume the parent of content dir is project dir
    PATH = os.path.dirname(instance.settings['PATH'])

    shared_dirs = ['highlights', 'members', 'projects', 'presentations', 'software']
    generated_pages = ['presentations.md', 'members.md', 'projects.md', 'software.md', 'publications.md', 'thesis-gallery.md']
    default_pages = ['colofon.md', '404.md', 'home.md']

    if instance.source_path:
        # Split the directories to check what kind of file we are building
        dirs = os.path.normpath(instance.source_path).split(os.path.sep)

        # Check if this is a shared file or not
        if any([f in instance.source_path for f in generated_pages]):
            rel_file_path = 'docs/generated.md'
            instance.edit_url = EDIT_CONTENT_URL.format(file_path=rel_file_path).replace('/edit', '/blob')
        elif any([f in instance.source_path for f in default_pages]):
            rel_file_path = 'docs/default_page.md'
            instance.edit_url = EDIT_CONTENT_URL.format(file_path=rel_file_path).replace('/edit', '/blob')
        elif any([dir in dirs for dir in shared_dirs]):
            rel_file_path = instance.source_path[len(PATH):].lstrip(os.path.sep)
            # Add replace for highlight (blog items)
            instance.edit_url = EDIT_CONTENT_URL.format(file_path=rel_file_path).replace('/content/highlights', '/content/pages/highlights')
        else:
            rel_file_path = WEBSITE + '/' + instance.source_path[len(PATH):].lstrip(os.path.sep)
            instance.edit_url = EDIT_CONTENT_URL.format(file_path=rel_file_path)

def register():
    signals.content_object_init.connect(add_edit_url)
