#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

#
# Site specific variables
# Please update these to customize the website.
#
AUTHOR = "AI for Anesthesiology"
SITENAME = "AI for Anesthesiology"
SITENAME_SHORT = "AI4A"
SITE_REPO = "website-ai4a"
SITE_GROUP = "ai4a"

# Home page and social settings
SITETITLE = "AI for Anesthesiology"
SITELEAD = """
The AI for Anesthesiology research group is a newly founded nationwide research collaboration that primarily focusses on the development and implementation of AI solutions for the anesthesiologists of the future.<br><br>
We offer a platform for research collaboration, MSc student projects and PhD projects.
"""
SITE_PICTURE = "images/general/AI4A.jpeg"

HOME_IMAGE = None #"images/general/AI4A.jpeg"
HOME_IMAGE_CAPTION = 'AI for Anesthesiology'

TWITTER_URL = None
FOOTER_TEXT = ""
TOP_DOMAIN = '<a href="https://anesthesiologie.nl">NVA</a>'
PARENT_DOMAIN = (
    ''
)
HOME_JUMBOTRON_LAYOUT = "neural-bg"

# Whether to show email buttons on every person circle
SHOW_EMAIL_GROUP_MEMBERS_INLINE = False

# What sections to show in the nav bar
NAV_SECTIONS = [
    {"name": "About", "url": "about", "icon_mobile": "info", "text_class": "d-lg-block"},
    {"name": "Reserarch groups", "url": "centers", "icon_mobile": "users", "text_class": "d-lg-block"},
    #{"name": "Highlights", "url": "highlights", "icon": "megaphone"},
    #{"name": "Members", "url": "members", "icon": "users"},
    #{"name": "Projects", "url": "projects", "icon": "folder"},
    #{"name": "Vacancies", "url": "vacancies", "icon": "vacancies"},
    #{"name": "Publications", "url": "publications", "icon": "file-text-o", "hidden": 95},
    #{"name": "Thesis Gallery", "url": "thesis-gallery", "icon": "book", "hidden": 95},
    {"name": "Contact", "url": "contact", "icon_mobile": "envelope-o", "text_class": "d-lg-block"},
]

# Whether to show breadcrumbs on the page
ENABLE_BREADCRUMBS = True

# What sections to show on homepage (current options that you customizable: {section_name: custom_name})
HOME_SECTIONS = {
    "News": "News",
}

# URLs
SITEURL = "https://aiforanesthesiology.nl"
IMGURL = SITEURL
EDIT_CONTENT_URL = (
    "https://github.com/AIforAnesthesiology/website-content/edit/master/{file_path}"
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

ARTICLE_URL = "news/{slug}/"
ARTICLE_SAVE_AS = "news/{slug}/index.html"
ARTICLE_TYPE = "News"

TAGS_SAVE_AS = ""
TAG_SAVE_AS = ""
CATEGORY_URL = ""
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""

ARCHIVES_SAVE_AS = ""
SITEMAP_SAVE_AS = "sitemap.xml"
INDEX_SAVE_AS = "news/index.html"

# Theme settings
THEME = "../radboudumc-template"
DIRECT_TEMPLATES = ["index", "sitemap"]

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
]
