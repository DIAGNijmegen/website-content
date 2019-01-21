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
    if EDIT_CONTENT_URL is None:
        return

    # assume the parent of content dir is project dir
    PATH = os.path.dirname(instance.settings['PATH'])

    if instance.source_path:
        rel_file_path = instance.source_path[len(PATH):].lstrip(os.path.sep)
        instance.edit_url = EDIT_CONTENT_URL.format(file_path=rel_file_path)


def register():
    signals.content_object_init.connect(add_edit_url)
