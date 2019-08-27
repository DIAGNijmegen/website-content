#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

#
# Site specific variables
# Please update these to customize the website.
#
AUTHOR = u'RTC'
SITENAME = u'RTC Deep Learning'
SITENAME_SHORT = 'RTC'
SITE_REPO = 'website-rtc'
SITE_GROUP = 'rtc'

# Home page and social settings
SITELEAD = 'The Radboudumc Technology Center (RTC) Deep Learning leverages the expertise of the Diagnostic Image Analysis Group (DIAG) in using machine learning, specifically deep learning, to analyze images and other medical data. RTC Deep Learning has set up a high-performance GPU cluster on which deep learning systems can be trained and deployed. We can be approached for consultation regarding all questions pertaining to the use of deep learning for specific problems. Additionally, we can make project-specific algorithms and commercial-grade web-based image analysis and data analytics software.<br><br> Our areas of expertise include: medical image analysis, development of deep learning algorithms, web-based image analysis and viewing applications and Docker and (cloud-based) GPU solutions.'
SITE_PICTURE = 'images/social/missing_picture_social.png'
HOME_IMAGE = 'images/general/ApplicationsOfDeepLearning.png'
HOME_IMAGE_CAPTION = ''
TWITTER_URL = 'https://twitter.com/diagnijmegen?ref_src=twsrc%5Etfw'
FOOTER_TEXT = 'RTC Deep Learning'
TOP_DOMAIN = '<a href="https://www.radboudumc.nl">Radboudumc</a>'
PARENT_DOMAIN = '<a href="http://www.radboudimaging.nl">Radboud Imaging</a>'

# What sections to show in the nav bar
NAV_SECTIONS = [
#     {"name": "Highlights", "url": "higlights", "icon": "megaphone"},
#     {"name": "Members", "url": "members", "icon": "users"},
#     {"name": "Projects", "url": "projects", "icon": "folder"},
#     {"name": "Vacancies", "url": "vacancies"},
#     {"name": "Publications", "url": "publications", "icon": "file-text-o", "hidden": 85},
#     {"name": "Presentations", "url": "presentations", "hidden": 95},
#     {"name": "Thesis Gallery", "url": "thesis-gallery", "icon": "book", "hidden": 95},
    {"name": "Contact", "url": "contact", "icon": "envelope-o", "hidden": 60},
]

# What sections to show on homepage (current options that you customizable: ["Projects", "Software"])
HOME_SECTIONS = ["Projects", "Software", "Members"]

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
ARTICLE_TYPE = 'Highlights'

TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''
CATEGORY_URL = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''

SITEMAP_SAVE_AS = 'sitemap.xml'
INDEX_SAVE_AS = 'highlights/index.html'

# Theme settings
THEME = "../radboudumc-template"
DIRECT_TEMPLATES = ['index', 'archives', 'sitemap']

# Plugins
PLUGIN_PATHS = ["../plugins"]
PLUGINS = ["bibtex",  "bibtex_loader", "edit_url", "hierarchy", "fileutil", "bootstrapify", "imgutil", "inline_extend", "member_data"]
