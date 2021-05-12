import os

from pelican import signals

def content_exists_or_default(paths, default):
    if type(paths) == str:
        paths = [paths]

    # Try to find a path that exists
    for path in paths:
        if os.path.isfile(os.path.join(os.getcwd(), '../assets', path)):
            return path

    return default

def sort_by_last(pages):
    """Simple filter to sort by last part of a slug instead of first char"""

    # Pages can be a generator if filters are used (like selectattr)
    return sorted(list(pages), key=lambda p: p.slug.split('-')[-1])

def add_filter(pelican):
    """Add filters."""
    pelican.env.filters.update({'content_exists_or_default': content_exists_or_default})
    pelican.env.filters.update({'sort_slug_by_last': sort_by_last})

def register():
    """Plugin registration."""
    signals.generator_init.connect(add_filter)
