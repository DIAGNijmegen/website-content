import os

from pelican import signals

def content_exists_or_default(path, default):
  if os.path.isfile(os.path.join( os.getcwd(), 'content', path)):
    return path
  else:
    return default

def add_filter(pelican):
    """Add filters."""
    pelican.env.filters.update({'content_exists_or_default': content_exists_or_default})

def register():
    """Plugin registration."""
    signals.generator_init.connect(add_filter)
