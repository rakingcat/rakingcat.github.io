#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'rakingcat'
SITENAME = "钉耙猫"
SITEURL = ''

PATH = 'content'
THEME = 'theme'
THEME_COLOR = 'blue'
SIDEBAR_DISPLAY = ['about', 'categories', 'tags']
SIDEBAR_ABOUT ="钉耙猫@rakingcat"

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

TIMEZONE = 'Asia/Shanghai'
DEFAULT_DATE_FORMAT = '%m/%d/%Y'
DEFAULT_LANG = 'zh_CN.UTF-8'
SUMMARY_MAX_LENGTH = 3

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_DATE ='fs'

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
)



DEFAULT_PAGINATION = False

STATIC_PATHS = ['images']
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
