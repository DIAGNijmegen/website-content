#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

CURRENTYEAR = date.today().year
AUTHOR = u'WebteamDIAG'
SITENAME = u'Computational Pathology Group'
SITENAME_SHORT = 'CPG'
SITE_PICTURE = 'images/computational_pathology_social_image.png'
SITEURL = ''
SITE_REPO = 'website-pathology'

# Home page and social settings
SITELEAD = 'The Computational Pathology Group develops, validates and deploys novel medical image analysis methods based on deep learning technology and focusing on computer-aided diagnosis. Application areas include diagnostics and prognostics of breast, prostate and colon cancer. We have rapidly expanded over the last few years, counting over 15 people today. Our group is among the international front runners in the field, witnessed for instance by our highly successful CAMELYON challenges. We have a strong translational focus, facilitated by our close collaboration with clinicians and industry.'
SITE_PICTURE = 'images/computational_pathology_social_image.png'
HOME_IMAGE = 'images/general/home-page-image.png'
HOME_IMAGE_CAPTION = 'Automated tumor detection'
TWITTER_URL = 'https://twitter.com/diagnijmegen?ref_src=twsrc%5Etfw'
FOOTER_TEXT = 'The Computational Pathology Group is part of the Department of Pathology at <a href="https://www.radboudumc.nl">Radboud University Medical Center</a>.'
TOP_DOMAIN = '<a href="https://www.radboudumc.nl">Radboudumc</a>'
PARENT_DOMAIN = '<a href="http://www.diagnijmegen.nl">Diagnostic Image Analysis Group</a>'

PATH = 'content'
RELATIVE_URLS = False

TIMEZONE = 'Europe/Amsterdam'

#DEFAULT_LANG = u'EN'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)
#THEME = 'pathology-theme'
DEFAULT_PAGINATION = 10

# URL settings
BIBKEYS_SRC = 'content/dict_pubs.json'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
SLUGIFY_SOURCE = 'basename'

ARTICLE_URL = 'highlights/{slug}/'
ARTICLE_SAVE_AS = 'highlights/{slug}/index.html'

CATEGORY_URL = 'categories/{slug}'
CATEGORY_SAVE_AS = 'categories/{slug}/index.html'
CATEGORIES_SAVE_AS = 'categories/index.html'

ARCHIVES_SAVE_AS = 'archives/index.html'

INDEX_SAVE_AS = 'highlights/index.html'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme settings
#
THEME = "../radboudumc-template"

# Plugins
#
PLUGIN_PATHS = ["../plugins"]
PLUGINS = ["bibtex",  "bibtex_loader", "edit_url", "hierarchy", "fileutil", "bootstrapify"]

# Other
EDIT_CONTENT_URL = 'https://github.com/diagnijmegen/website-content/edit/master/{file_path}'
