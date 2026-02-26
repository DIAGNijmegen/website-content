#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

#
# Site specific variables
# Please update these to customize the website.

AUTHOR = "WebteamDIAG"
SITENAME = "CARA Lab"
SITENAME_SHORT = "CARALAB"
SITE_REPO = "website-cara-lab"
SITE_GROUP = "cara-lab"

# Home page and social settings
SITETITLE = "CARA Lab"
SITELEAD = 'Towards robust and trustworthy AI-systems for real-time analysis of optical coherence tomography (OCT) images at the cardiac catheterization lab.'
SITE_PICTURE = 'images/social/missing_picture_social.png'
HOME_IMAGE = 'images/general/cara_lab_home2.png'
HOME_IMAGE_CAPTION = 'CARA Lab'
NUM_NEWS_HOME_PAGE = 4
TWITTER_URL = None
FOOTER_TEXT = 'CARA Lab -- Cardiology Lab Radboudumc Amsterdam UMC'
TOP_DOMAIN = '<a href="https://www.radboudumc.nl">Radboudumc</a>'
PARENT_DOMAIN = '<a href="https://www.amc.nl/web/home.htm">Amsterdam UMC</a>'

CSS_THEME = "cara-theme"
FOOTER_IMAGE = 'cara_logo_new.png'
HOME_JUMBOTRON_LAYOUT = "dense"

# What sections to show in the nav bar
NAV_SECTIONS = [
    {
        "name": "About",
        "url": "about",
        "icon": "info",
    },
    {"name": "News", "url": "news", "icon": "megaphone"},
    {"name": "Members", "url": "members", "icon": "users"},
    {"name": "Algorithms", "url": "algorithms", "icon": "code"},
    {"name": "Vacancies", "url": "vacancies", "icon": "vacancies"},
    {"name": "Publications", "url": "publications", "icon": "file-text-o"},
    {"name": "Presentations", "url": "presentations", "hidden": 95},
    {"name": "Contact", "url": "contact", "icon": "envelope-o", "hidden": 60},
]

HOME_SECTIONS = {"News": "News", "Vacancies": "Vacancies",}

# Whether to show breadcrumbs on the page
ENABLE_BREADCRUMBS = True

# URLs
SITEURL = ''
IMGURL = SITEURL
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
TODAY = date.today()
LINKS = ()
DEFAULT_PAGINATION = 10

# URL settings
BIBKEYS_SRC = 'content/dict_pubs.json'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
SLUGIFY_SOURCE = 'basename'

ARTICLE_URL = 'news/{slug}/'
ARTICLE_SAVE_AS = 'news/{slug}/index.html'
ARTICLE_TYPE = 'News'

TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''
CATEGORY_URL = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''

SITEMAP_SAVE_AS = 'sitemap.xml'
INDEX_SAVE_AS = 'news/index.html'

# Theme settings
THEME = "../radboudumc-template"
DIRECT_TEMPLATES = ['index', 'archives', 'sitemap']

NO_CRITICAL_CSS = True

# Plugins
PLUGIN_PATHS = ["../plugins"]
PLUGINS = ["bibtex",  "bibtex_loader", "edit_url", "hierarchy", "fileutil", "grouputil", "bootstrapify", "imgutil", "inline_extend", "content_aggregator"]
