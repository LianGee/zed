import traceback

from flask import Flask, request
from flask_cors import CORS
from flask_session import Session

import config
from common.log import Logger
from common.response import Response
from model.db import clean_db_session
from view.album import album_bp
from view.article import article_bp
from view.catalogue import catalogue_bp
from view.graph import graph_bp
from view.tag import tag_bp
from view.test import test_bp
from view.user import user_bp
from view.weekly import weekly_bp
from view.workspace import workspace_bp

app = Flask(__name__)
log = Logger(__name__)
app.config.from_object(config)
CORS(app, supports_credentials=True)
Session(app)
app.register_blueprint(test_bp, url_prefix='/test')
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(article_bp, url_prefix='/article')
app.register_blueprint(graph_bp, url_prefix='/graph')
app.register_blueprint(tag_bp, url_prefix='/tag')
app.register_blueprint(catalogue_bp, url_prefix='/catalogue')
app.register_blueprint(album_bp, url_prefix='/album')
app.register_blueprint(workspace_bp, url_prefix='/workspace')
app.register_blueprint(weekly_bp, url_prefix='/weekly')


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.before_request
def before_request():
    log.info(request)


@app.after_request
def after_request(response):
    if response.json:
        log.info(response)
    return response


@app.teardown_request
def teardown_request(error):
    clean_db_session()
    if error is not None:
        log.error(error)


@app.errorhandler(Exception)
def error_handler(exception: Exception):
    if exception:
        log.error(traceback.format_exc())
        return Response.failed(msg=f'{exception}')


if __name__ == '__main__':
    app.run()
