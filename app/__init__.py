#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from flask import Flask
from flask_wtf import CsrfProtect
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
CsrfProtect(app)

from app import views

db = SQLAlchemy(app)