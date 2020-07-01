#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

CURRENTYEAR = date.today().year
TODAY = date.today()
AUTHOR = u'WebteamDIAG'
SITENAME = u'Computational Pathology Group'
SITENAME_SHORT = 'CPG'
SITEURL = ''
IMGURL = SITEURL
SITE_REPO = 'website-pathology'
SITE_GROUP = 'pathology'

# Home page and social settings
SITELEAD = 'The Computational Pathology Group develops, validates and deploys novel medical image analysis methods based on deep learning technology.'
SITE_PICTURE = 'images/social/computational_pathology_social_image.png'
HOME_IMAGE = 'images/general/home-page-image.png'
HOME_IMAGE_CAPTION = 'Automated tumor detection'
TWITTER_URL = 'https://twitter.com/diagnijmegen?ref_src=twsrc%5Etfw'
FOOTER_TEXT = 'The Computational Pathology Group is part of the Department of Pathology at <a href="https://www.radboudumc.nl">Radboud University Medical Center</a>.'
TOP_DOMAIN = '<a href="https://www.radboudumc.nl">Radboudumc</a>'
PARENT_DOMAIN = '<a href="http://www.diagnijmegen.nl">Diagnostic Image Analysis Group</a>'
HOME_JUMBOTRON_LAYOUT = 'dense'

# What sections to show in the nav bar
NAV_SECTIONS = [
    {"name": "Highlights", "url": "highlights", "icon": "megaphone"},
    {"name": "Members", "url": "members", "icon": "users"},
    {"name": "Projects", "url": "projects", "icon": "folder"},
    {"name": "Vacancies", "url": "vacancies", "icon": "vacancies"},
    {"name": "Publications", "url": "publications", "icon": "file-text-o", "hidden": 85},
    {"name": "Presentations", "url": "presentations", "icon": "presentations", "hidden": 95},
    {"name": "Thesis Gallery", "url": "thesis-gallery", "icon": "book", "hidden": 95},
    {"name": "Contact", "url": "contact", "icon": "envelope-o", "hidden": 60},
]

# What sections to show on homepage (current options that you customizable: {section_name: custom_name})
HOME_SECTIONS = {"Highlights": 'Highlights', "Vacancies": "Vacancies", "Projects": "Projects", "Members": 'Members'}

PATH = 'content'
RELATIVE_URLS = False

# Show pdf request on publication pages
# ENABLE_PUBLICATION_PDF_REQUEST = True

# show publication years
# SHOW_PUBLICATION_YEARS = False

TIMEZONE = 'Europe/Amsterdam'
DEFAULT_LANG = 'EN'
ARTICLE_TRANSLATION_ID = None
PAGE_TRANSLATION_ID = None

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)
#THEME = 'pathology-theme'
DEFAULT_PAGINATION = 10
MAX_YEAR_PUB = 2012

# URL settings
BIBKEYS_SRC = 'content/dict_pubs.json'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
SLUGIFY_SOURCE = 'basename'

ARTICLE_URL = 'highlights/{slug}/'
ARTICLE_SAVE_AS = 'highlights/{slug}/index.html'
ARTICLE_TYPE = 'Highlights'

CATEGORY_URL = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''

ARCHIVES_SAVE_AS = ''

SITEMAP_SAVE_AS = 'sitemap.xml'
INDEX_SAVE_AS = 'highlights/index.html'


# Theme settings
THEME = "../radboudumc-template"
DIRECT_TEMPLATES = ['index', 'archives', 'sitemap']

# Plugins
#
PLUGIN_PATHS = ["../plugins"]
PLUGINS = ["bibtex",  "bibtex_loader", "edit_url", "hierarchy", "fileutil", "bootstrapify", "imgutil", "inline_extend", "content_aggregator"]

# Other
EDIT_CONTENT_URL = 'https://github.com/diagnijmegen/website-content/edit/master/{file_path}'
STATIC_PATHS = ['images', 'dzi']
