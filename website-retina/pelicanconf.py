#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

#
# Site specific variables
# Please update these to customize the website.
#
AUTHOR = u'WebteamDIAG'
SITENAME = u'A-eye Research Group'
SITENAME_SHORT = 'A-eye'
SITE_REPO = 'website-retina'

# Home page and social settings
SITELEAD = 'The A-eye Research Group focuses on computer-aided techniques based on artificial intelligence for detection, diagnosis and quantification of retinal diseases.'
SITE_PICTURE = 'images/general/retina_main.JPG'
HOME_IMAGE = 'images/general/retina_main.JPG'
#HOME_IMAGE_CAPTION = 'Automated tumor detection'
TWITTER_URL = 'https://twitter.com/diagnijmegen?ref_src=twsrc%5Etfw'
FOOTER_TEXT = 'The A-eye Research Group is part of <a href="https://www.radboudumc.nl">Radboud University Medical Center</a>.'
TOP_DOMAIN = '<a href="https://www.radboudumc.nl">Radboudumc</a>'
PARENT_DOMAIN = '<a href="http://www.diagnijmegen.nl">Diagnostic Image Analysis Group</a>'

# URLs
SITEURL = ''
EDIT_CONTENT_URL = 'https://github.com/diagnijmegen/website-content/edit/master/{file_path}'

#
# Non-content variables
# In general these values do not have to be changed.
#
PATH = 'content'
RELATIVE_URLS = False

TIMEZONE = 'Europe/Amsterdam'
DEFAULT_LANG = 'EN'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

CURRENTYEAR = date.today().year
LINKS = ()
DEFAULT_PAGINATION = 10

# URL settings
BIBKEYS_SRC = 'content/dict_pubs.json'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
SLUGIFY_SOURCE = 'basename'

ARTICLE_URL = 'highlights/{slug}/'
ARTICLE_SAVE_AS = 'highlights/{slug}/index.html'

CATEGORY_URL = 'categories/{slug}'
CATEGORY_SAVE_AS = 'categories/{slug}/index.html'
CATEGORIES_SAVE_AS = 'categories/index.html'

ARCHIVES_SAVE_AS = 'archives/index.html'

INDEX_SAVE_AS = 'highlights/index.html'

# Theme settings
THEME = "../radboudumc-template"

# Plugins
PLUGIN_PATHS = ["../plugins"]
PLUGINS = ["bibtex",  "bibtex_loader", "edit_url", "hierarchy", "fileutil"]
