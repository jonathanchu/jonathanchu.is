#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from os import environ

AUTHOR = 'Jonathan Chu'
SITENAME = 'jonathanchu.is'
EMAIL = 'me@jonathanchu.is'
SITEURL = environ.get('PELICAN_SITEURL', 'http://jonathanchu.is')

THEME = 'theme'

PATH = 'content'

TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

DEFAULT_PAGINATION = 10

RELATIVE_URLS = False

DIRECT_TEMPLATES = ('index', 'posts_index')
PAGINATED_DIRECT_TEMPLATES = ('index', 'posts_index')

POSTS_URL = 'posts/'
POSTS_INDEX_SAVE_AS = 'posts/index.html'

ARTICLE_PATHS = ['posts']
ARTICLE_URL = 'posts/{slug}/'
ARTICLE_SAVE_AS = 'posts/{slug}/index.html'

TAG_URL = 'posts/tags/{slug}/'
TAG_SAVE_AS = 'posts/tags/{slug}/index.html'
TAGS_SAVE_AS = 'posts/tags/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

FEED_RSS = 'posts/feed/latest'
FEED_ATOM = 'posts/feed/latest.atom'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['assets']

ASSET_SOURCE_PATHS = ['static']

MIXPANEL = ''
