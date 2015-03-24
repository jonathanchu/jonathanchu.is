#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from os import environ

AUTHOR = 'Jonathan Chu'
SITENAME = 'jonathanchu.is'
EMAIL = ''
SITEURL = environ.get('PELICAN_SITEURL', 'http://jonathanchu.is')

PATH = 'content'

TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

DEFAULT_PAGINATION = 10

RELATIVE_URLS = False

MIXPANEL = ''
