import os

from pelican import signals

def content_exists_or_default(paths, default):
    if type(paths) == str:
        paths = [paths]

    # Try to find a path that exists
    for path in paths:
      if os.path.isfile(os.path.join(os.getcwd(), 'content', path)):
        return path

    return default

def add_filter(pelican):
    """Add filters."""
    pelican.env.filters.update({'content_exists_or_default': content_exists_or_default})

def register():
    """Plugin registration."""
    signals.generator_init.connect(add_filter)
