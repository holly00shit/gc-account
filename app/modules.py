#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from app import db

class Acounts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    expense = db.Column(db.Integer)
    income = db.Column(db.Integer)
    post_time = db.Column(db.DateTime)


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), unique = True)
    last_seen = db.Column(db.DateTime)
