#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os
basedir = os.path.abspath(os.path.dirname(__file__))

#app config
SECRET_KEY = "Z\xd1L\xa2wb\x11\xc8\xd2\x12\xdb\xd2\x06\xb9\xcd\xab\xd2\x8bLv\x8e\xd9\xd3\xdb"
PERMANENT_SESSION_LIFETIME = 3600 * 24 * 7
SESSION_COOKIE_NAME = 'gc_session'

#db config
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db/app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db/db_repository')

