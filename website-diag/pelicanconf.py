#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date
import sys
import importlib

#
# Site specific variables
# Please update these to customize the website.
#
AUTHOR = u'WebteamDIAG'
SITENAME = u'Diagnostic Image Analysis Group'
SITENAME_SHORT = 'DIAG'
SITE_REPO = 'website-diag'
SITE_GROUP = 'diag'

# Home page, layout and social settings
SITELEAD = 'The Diagnostic Image Analysis Group is part of the Departments of Imaging, Pathology, Ophthalmology, and Radiation Oncology of Radboud University Medical Center. We develop computer algorithms to interpret and process medical images.'
SITE_PICTURE = 'images/social/missing_picture_social.png'
HOME_IMAGE = 'highlight'
HOME_IMAGE_CAPTION = 'Different applications of deep learning.'
TWITTER_URL = None
FOOTER_TEXT = 'The Diagnostic Image Analysis Group is part of the <a href="https://www.radboudumc.nl">Radboud University Medical Center</a>.'
TOP_DOMAIN = '<a href="https://www.radboudumc.nl">Radboudumc</a>'
PARENT_DOMAIN = '<a href="http://www.radboudimaging.nl">Radboud Imaging</a>'
HOME_JUMBOTRON_LAYOUT = 'dense'

# What sections to show in the nav bar
# For diag the text is shown in viewports lg and up, below that only the icon is shown
# d-lg-block is used to force to show the text on lg viewports, for other websites there is not
# enought room to show the text.
NAV_SECTIONS = [
    {"name": "About", "url": "about", "icon_mobile": "info", "text_class": "d-lg-block"},
    {"name": "People", "url": "people", "icon_mobile": "users", "text_class": "d-lg-block"},
    {"name": "Research", "url": "research", "icon_mobile": "folder", "text_class": "d-lg-block"},
    {"name": "Publications", "url": "publications", "icon_mobile": "file-text-o", "text_class": "d-lg-block"},
    {"name": "Vacancies", "url": "vacancies", "icon_mobile": "vacancies", "text_class": "d-lg-block"},
    {"name": "Contact", "url": "contact", "icon_mobile": "envelope-o", "text_class": "d-lg-block"},
]

# What sections to show on homepage (current options that you customizable: {section_name: custom_name})
HOME_SECTIONS = {"Highlights": 'Highlights', "Vacancies": "Vacancies"}

# Whether to show breadcrumbs on the page
ENABLE_BREADCRUMBS = False

# Show membership of people on their page
SHOW_GROUP_MEMBERSHIP = True

# URLs
SITEURL = ''
IMGURL = SITEURL
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
TODAY = date.today()
LINKS = ()
DEFAULT_PAGINATION = 10

# URL settings
BIBKEYS_SRC = 'content/dict_pubs.json'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
PAGE_MEMBERS_SAVE_AS = 'people/{slug}/index.html'
PAGE_MEMBERS_URL = 'people/{slug}/'
SLUGIFY_SOURCE = 'basename'

ARTICLE_URL = 'news/{slug}/'
ARTICLE_SAVE_AS = 'news/{slug}/index.html'
ARTICLE_TYPE = 'News'

TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''
CATEGORY_URL = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''

ARCHIVES_SAVE_AS = ''
SITEMAP_SAVE_AS = 'sitemap.xml'
INDEX_SAVE_AS = 'news/index.html'

# Theme settings
THEME = "../radboudumc-template"
DIRECT_TEMPLATES = ['index', 'archives', 'sitemap']

# Plugins
PLUGIN_PATHS = ["../plugins"]
PLUGINS = ["bibtex",  "bibtex_loader", "edit_url", "hierarchy", "fileutil", "bootstrapify", "imgutil", "inline_extend", "content_aggregator"]
