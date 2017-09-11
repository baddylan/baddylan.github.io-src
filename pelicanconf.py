#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Dylan Copeland'
SITENAME = u'Faded Stars News.'
SITEURL = 'http://news.fadedstars.xyz'

STATIC_PATHS = ['extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'

DEFAULT_DATE= 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),
         ('Github Source Code Page', 'https://github.com/baddylan/baddylan.github.io-src'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#Slugify
SLUGIFY_SOURCE = 'title'

# Plugins
PLUGIN_PATHS = ["plugins/pelican-plugins"]
PLUGINS = ["tag_cloud", "custom_article_urls"]
