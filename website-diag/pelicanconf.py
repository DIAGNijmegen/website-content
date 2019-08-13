#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date
import sys
import importlib

# Load configs from all other websites
sys.path.insert(0, '../')
DIAG_WEBSITES_CONFIG = {}
DIAG_WEBSITE_URLS = {}
for website in ['website-pathology', 'website-retina', 'website-bodyct', 'website-aiimnijmegen', 'website-neuro', 'website-rse']:
    DIAG_WEBSITES_CONFIG[website[8:]] = importlib.import_module(f'{website}.pelicanconf')
    DIAG_WEBSITE_URLS[website[8:]] = importlib.import_module(f'{website}.publishconf').SITEURL

#
# Site specific variables
# Please update these to customize the website.
#
AUTHOR = u'WebteamDIAG'
SITENAME = u'Diagnostic Image Analysis Group'
SITENAME_SHORT = 'DIAG'
SITE_REPO = 'website-diag'

# Home page and social settings
SITELEAD = 'The Diagnostic Image Analysis Group is part of the Departments of Radiology and Nuclear Medicine, Pathology, and Ophthalmology of Radboud University Medical Center. We develop computer algorithms to aid clinicians in the interpretation of medical images and thereby improve the diagnostic process.'
SITE_PICTURE = 'images/missing_picture_social.png'
HOME_IMAGE = 'images/general/ApplicationsOfDeepLearning.png'
HOME_IMAGE_CAPTION = 'Differnt applications of deep learning.'
TWITTER_URL = 'https://twitter.com/diagnijmegen?ref_src=twsrc%5Etfw'
FOOTER_TEXT = 'The Diagnostic Image Analysis Group is part of the Department of Radiology and Nuclear Medicine at <a href="https://www.radboudumc.nl">Radboud University Medical Center</a>.'
TOP_DOMAIN = '<a href="https://www.radboudumc.nl">Radboudumc</a>'
PARENT_DOMAIN = '<a href="http://www.radboudimaging.nl">Radboud Imaging</a>'

# What sections to show in the nav bar
NAV_SECTIONS = [
    {"name": "Highlights", "url": "highlights", "icon": "megaphone"},
    {"name": "Members", "url": "members", "icon": "users"},
    {"name": "Research", "url": "research", "icon": "folder"},
    {"name": "Vacancies", "url": "vacancies"},
    {"name": "Publications", "url": "publications", "icon": "file-text-o", "hidden": 85},
    {"name": "Presentations", "url": "presentations", "hidden": 95},
    {"name": "Thesis Gallery", "url": "thesis-gallery", "icon": "book", "hidden": 95},
    {"name": "Contact", "url": "contact", "icon": "envelope-o", "hidden": 60},
]

# What sections to show on homepage (current options that you customizable: ["Projects", "Software"])
HOME_SECTIONS = ["Highlights", "Calendar"]

# Show membership of people on their page
SHOW_GROUP_MEMBERSHIP = True

# URLs
SITEURL = ''
EDIT_CONTENT_URL = 'https://github.com/diagnijmegen/website-content/edit/master/{file_path}'

# Show pdf request on publication pages
ENABLE_PUBLICATION_PDF_REQUEST = True

#
# Non-content variables
# In general these values do not have to be changed.
#
PATH = 'content'
RELATIVE_URLS = False

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

TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''
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
PLUGIN_PATHS = ["../plugins"]
PLUGINS = ["bibtex",  "bibtex_loader", "edit_url", "hierarchy", "fileutil", "bootstrapify", "imgutil"]
