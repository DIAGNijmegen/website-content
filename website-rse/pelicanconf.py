#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

#
# Site specific variables
# Please update these to customize the website.
#
AUTHOR = "DIAG RSE"
SITENAME = "DIAG Research Software Engineering"
SITENAME_SHORT = "DIAG RSE"
SITE_REPO = "website-rse"
SITE_GROUP = "rse"

# Home page and social settings
SITELEAD = """
The Research Software Engineering Team is part of the Diagnostic Image Analysis Group at Radboud University Medical Center in Nijmegen, The Netherlands.<br><br>
We use industry best practices to develop software that enables researchers to rapidly develop novel machine learning algorithms that we can integrate into research workstations for clinical validation.
"""
SITE_PICTURE = "images/social/missing_picture_social.png"
HOME_IMAGE = "images/general/ApplicationsOfDeepLearning.png"
HOME_IMAGE_CAPTION = ""
NUM_NEWS_HOME_PAGE = 4
TWITTER_URL = "https://twitter.com/diagnijmegen?ref_src=twsrc%5Etfw"
FOOTER_TEXT = ""
TOP_DOMAIN = '<a href="https://www.radboudumc.nl">Radboudumc</a>'
PARENT_DOMAIN = '<a href="http://www.radboudimaging.nl">Radboud Imaging</a>'
FOOTER_IMAGE = 'umc_logo.png'

# What sections to show in the nav bar
NAV_SECTIONS = [
    # {"name": "Highlights", "icon": "megaphone"},
    {"name": "People", "url": "members", "icon": "users"},
    # {"name": "Projects", "url": "projects", "icon": "folder"},
    {"name": "Software", "url": "software", "icon": "code"},
    {"name": "Vacancies", "url": "vacancies", "icon": "vacancies"},
    {"name": "Contact", "url": "contact", "icon": "envelope-o"},
]

# Whether to show breadcrumbs on the page
ENABLE_BREADCRUMBS = True

# What sections to show on homepage (current options that you customizable: {section_name: custom_name})
HOME_SECTIONS = {"Vacancies": "Vacancies", "Software": "Software"}

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

ARCHIVES_SAVE_AS = ""

SITEMAP_SAVE_AS = "sitemap.xml"
INDEX_SAVE_AS = "highlights/index.html"

# Theme settings
THEME = "../radboudumc-template"
DIRECT_TEMPLATES = ["index", "archives", "sitemap"]

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
