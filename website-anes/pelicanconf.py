#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

#
# Site specific variables
# Please update these to customize the website.

AUTHOR = "Rob Tolboom"
SITENAME = "Department of Anesthesiology"
SITENAME_SHORT = "ANES"
SITE_REPO = "website-anes"
SITE_GROUP = "anes"

# Home page and social settings
SITETITLE = "Anesthesiology"
SITELEAD = 'Overview of all science and innovation projects at our department of Anesthesiology.'
SITE_PICTURE = 'images/social/missing_picture_social.png'
HOME_IMAGE = 'images/general/home-page-cara.png'
HOME_IMAGE_CAPTION = 'CARA Lab'
NUM_NEWS_HOME_PAGE = 4
TWITTER_URL = None
FOOTER_TEXT = ''
TOP_DOMAIN = '<a href="https://www.umcg.nl">UMCG</a>'
PARENT_DOMAIN = '<a href="https://www.umcg.nl/">Sector ... (niet werkzame link)</a>'
THIRD_DOMAIN = ''
CSS_THEME = "anes-theme"
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
    {"name": "Vacancies", "url": "vacancies", "icon": "vacancies"},
    {"name": "Publications", "url": "publications", "icon": "file-text-o", "hidden": 85},
    {"name": "Presentations", "url": "presentations", "hidden": 95},
    {"name": "Contact", "url": "contact", "icon": "envelope-o", "hidden": 60},
]

HOME_SECTIONS = {"News": "News", "Vacancies": "Vacancies",}

# Whether to show breadcrumbs on the page
ENABLE_BREADCRUMBS = True

# URLs
SITEURL = ''
IMGURL = SITEURL
EDIT_CONTENT_URL = 'https://github.com/RobTolboom/umcg-anesthesie/edit/master/{file_path}'

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
