#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

#
# Site specific variables
# Please update these to customize the website.
#
AUTHOR = "RTC"
SITENAME = "RTC Deep Learning"
SITENAME_SHORT = "RTC"
SITE_REPO = "website-rtc"
SITE_GROUP = "rtc"

# Home page and social settings
SITELEAD = "We use Artificial Intelligence, specifically Deep Learning, to analyze medical images and other medical data. We have set up a high-performance GPU cluster on which deep learning systems can be trained and deployed. We provide advise and develop algorithms and web-based image analysis and data analytics software."
SITE_PICTURE = "images/social/missing_picture_social.png"
HOME_IMAGE = "images/general/rtc-2.jpg"
HOME_IMAGE_CAPTION = ""
NUM_NEWS_HOME_PAGE = 4
TWITTER_URL = "https://twitter.com/diagnijmegen?ref_src=twsrc%5Etfw"
FOOTER_TEXT = ""
TOP_DOMAIN = '<a href="https://www.radboudumc.nl">Radboudumc</a>'
PARENT_DOMAIN = '<a href="http://www.radboudimaging.nl">Radboud Imaging</a>'
HOME_JUMBOTRON_LAYOUT = "neural-bg"
FOOTER_IMAGE = 'umc_logo.png'

# What sections to show in the nav bar
NAV_SECTIONS = [
    #     {"name": "Highlights", "url": "higlights", "icon": "megaphone"},
    {"name": "Members", "url": "members", "icon": "users"},
    #     {"name": "Projects", "url": "projects", "icon": "folder"},
    #     {"name": "Vacancies", "url": "vacancies"},
    {
        "name": "Publications",
        "url": "publications",
        "icon": "file-text-o",
        "hidden": 85,
    },
    #     {"name": "Presentations", "url": "presentations", "hidden": 95},
    #     {"name": "Thesis Gallery", "url": "thesis-gallery", "icon": "book", "hidden": 95},
    {"name": "Contact", "url": "contact", "icon": "envelope-o", "hidden": 60},
]

# Whether to show breadcrumbs on the page
ENABLE_BREADCRUMBS = True

# What sections to show on homepage (current options that you customizable: {section_name: custom_name})#"Services and expertise": "Services and expertise",
HOME_SECTIONS = {
    "Services and expertise": "Services and expertise",
    "Projects": "Projects",
    "Software": "Infrastructure & Software",
}

# URLs
SITEURL = ""
IMGURL = SITEURL
EDIT_CONTENT_URL = (
    "https://github.com/diagnijmegen/website-content/edit/master/{file_path}"
)

#
# Non-content variables
# In general these values do not have to be changed.
#
PATH = "content"
RELATIVE_URLS = False

# Show pdf request on publication pages
ENABLE_PUBLICATION_PDF_REQUEST = False

TIMEZONE = "Europe/Amsterdam"
DEFAULT_LANG = "EN"
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
BIBKEYS_SRC = "content/dict_pubs.json"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
SLUGIFY_SOURCE = "basename"

ARTICLE_URL = "highlights/{slug}/"
ARTICLE_SAVE_AS = "highlights/{slug}/index.html"
ARTICLE_TYPE = "Highlights"

TAGS_SAVE_AS = ""
TAG_SAVE_AS = ""
CATEGORY_URL = ""
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""

SITEMAP_SAVE_AS = "sitemap.xml"
INDEX_SAVE_AS = "highlights/index.html"

# Theme settings
THEME = "../radboudumc-template"
DIRECT_TEMPLATES = ["index", "archives", "sitemap"]


ARTICLE_EXCLUDES = ['templates']
TEMPLATE_PAGES = {
    'templates/homepage.html': 'index.html',
}

# Plugins
PLUGIN_PATHS = ["../plugins"]
PLUGINS = [
    "bibtex",
    "bibtex_loader",
    "edit_url",
    "hierarchy",
    "fileutil",
    "bootstrapify",
    "imgutil",
    "inline_extend",
    "content_aggregator",
    "grouputil",
]
