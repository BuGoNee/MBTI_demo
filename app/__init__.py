#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'BuGoNee'


'''
Some Explaination should be in here.
'''
import os
import sys
sys.path.append(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0])

from sklearn.externals import joblib
regrs = joblib.load('app/mbti_models.pkl')
print 'initializing regrs:', regrs

from config import basedir
from flask import Flask
from flask.json import JSONEncoder

app = Flask(__name__)
app.config.from_object('config')

from flask_bootstrap import Bootstrap
app.config['SECRET_KEY'] = 'very hard to guess string'
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
bootstrap = Bootstrap(app)

from app import views



if __name__ == '__main__':
    pass
