# -*- coding: utf-8 -*-

from app import app
from flask import render_template

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/query_account')
def query_account():
    return render_template('query.html', title='query')

@app.route('/insert_account')
def insert_account():
    return render_template('insert.html', title='insert')