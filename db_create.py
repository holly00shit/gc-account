#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO
from app import db

db.create_all()
