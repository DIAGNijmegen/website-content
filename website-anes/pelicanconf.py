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
SITELEAD = 'Overview of all current and past science and innovation projects at our department of Anesthesiology.'
SITE_PICTURE = 'images/social/missing_picture_social.png'
HOME_IMAGE = 'images/general/UMCG.jpg'
HOME_IMAGE_CAPTION = ''
NUM_NEWS_HOME_PAGE = 4
TWITTER_URL = None
FOOTER_TEXT = ''
TOP_DOMAIN = '<a href="https://www.umcg.nl">UMCG</a>'
PARENT_DOMAIN = '<a href="https://www.umcg.nl/">Cluster Acute, Perioperative and Intensicve Care Medicine</a>'
THIRD_DOMAIN = ''
CSS_THEME = "anes-theme"
FOOTER_IMAGE = 'umcg.png'
HOME_JUMBOTRON_LAYOUT = "neural-bg"

# What sections to show in the nav bar
NAV_SECTIONS = [
    {
        "name": "About",
        "url": "about",
        "icon_mobile": "info",
        "text_class": "d-lg-block",
    },
    {   
        "name": "News", 
        "url": "news", 
        "icon_mobile": "megaphone", 
        "text_class": "d-lg-block",
    },
    {
        "name": "Members", 
        "url": "members", 
        "icon_mobile": "users", 
        "text_class": "d-lg-block",},
    {
        "name": "Research",
        "url": "research",
        "icon_mobile": "folder",
        "text_class": "d-lg-block",
    },
    {
        "name": "Publications", 
        "url": f"publications/{PUBLICATIONSYEAR}", 
        "icon_mobile": "file-text-o",
        "text_class": "d-lg-block",
    },
    {
        "name": "Thesis Gallery",
        "url": "thesis-gallery",
        "icon_mobile": "book",
        "text_class": "d-lg-block",
    },
    {
        "name": "Vacancies", 
        "url": "vacancies", 
        "icon_mobile": "vacancies",
        "text_class": "d-lg-block",
    },
    {
        "name": "Contact", 
        "url": "contact", 
        "icon_mobile": "envelope-o",
        "text_class": "d-lg-block",
    },
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
