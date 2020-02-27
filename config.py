#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : config.py
# @Author: zaoshu
# @Date  : 2020-02-06
# @Desc  :

import os

APP_NAME = 'zed'
SECRET_KEY = 'XKCWJC6KN99GRZPOYDJTALF45WG3RNQ9'
JSONIFY_PRETTYPRINT_REGULAR = True
JSON_AS_ASCII = False
DEBUG = True
ADDRESS = '0.0.0.0'
PORT = 5000
WORKERS = 4
FLASK_USE_RELOAD = True
BASE_DIR = os.path.abspath(os.getcwd())
EXCEL_PATH = BASE_DIR + '/data/excel/'
EXCEL_EXPORT = {
    'encoding': 'utf_8_sig',
}
DEFAULT_DATABASE_URL = 'mysql+mysqlconnector://root:123456@localhost:3306/zed?charset=utf8'
DB_KWARGS = {
    'pool_recycle': 360,
    'pool_size': 100,
    'max_overflow': 10,
    'logging_name': 'sqlalchemy',
}
DATABASES = {
    "default": DEFAULT_DATABASE_URL,
}

QI_NIU = {
    'access_key': 'qVMkbrZVpr5ZSgcS50ucro1m36zhL9FqqPfjUNgO',
    'secret_key': 'v2fMZffT-gQTTHnm7YFO4lSPnDINYE4EgxSxWaZc',
    'img_bucket_name': 'zedimg',
    'doc_bucket_name': 'zeddoc',
    'img_bucket_url': 'http://q5lfszjdu.bkt.clouddn.com/',
    'doc_bucket_url': 'http://q5lfxctru.bkt.clouddn.com/'
}
