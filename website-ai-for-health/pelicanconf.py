#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

#
# Site specific variables
# Please update these to customize the website.
#
AUTHOR = u'WebteamDIAG'
SITENAME = u'Radboud AI for Health'
SITENAME_SHORT = 'AIHEALTH'
SITE_REPO = 'website-ai-for-health'
SITE_GROUP = 'ai-for-health'

# Home page and social settings
SITETITLE = 'Radboud AI for Health'
SITELEAD = 'Radboud AI for Health is an ICAI lab where Radboud University and Radboudumc collaborate to create AI innovations in healthcare. We offer courses for professionals, BSc/MSc student projects and PhD projects.'
SITE_PICTURE ='images/social/missing_picture_social.png'

HOME_IMAGE = None
HOME_IMAGE_CAPTION = 'example picture'

TWITTER_URL = None
FOOTER_TEXT = ''
TOP_DOMAIN = '<a href="https://www.radboudumc.nl">Radboudumc</a>'
#PARENT_DOMAIN = '<a href="http://www.radboudimaging.nl">Radboud Imaging</a>'

# Whether to show email buttons on every person circle
SHOW_EMAIL_GROUP_MEMBERS_INLINE = True

# What sections to show in the nav bar
NAV_SECTIONS = [
    {"name": "Contact", "url": "contact", "icon": "envelope-o"},
]


# What sections to show on homepage (current options that you customizable: {section_name: custom_name})
HOME_SECTIONS = {"News": 'News', "PageCards": "PageCards"}


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

ARCHIVES_SAVE_AS = ''
SITEMAP_SAVE_AS = 'sitemap.xml'
INDEX_SAVE_AS = 'news/index.html'
# Theme settings
THEME = "../radboudumc-template"
DIRECT_TEMPLATES = ['index', 'sitemap']

# Plugins
PLUGIN_PATHS = ["../plugins"]
PLUGINS = ["edit_url", "hierarchy", "fileutil", "bootstrapify", "imgutil", "inline_extend", "content_aggregator"]
