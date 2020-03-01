#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : article.py
# @Author: zaoshu
# @Date  : 2020-02-13
# @Desc  :

from flask import Blueprint, request, g

from common.loged import log_this
from common.login import login_required
from common.response import Response
from service.article_service import ArticleService
from service.qiniu_service import QiniuService

article_bp = Blueprint('article', __name__)


@article_bp.route('/upload/img', methods=['POST'])
@login_required
@log_this
def upload_img():
    files = request.files
    file = files.get('file')
    url = ''
    if file is not None:
        if file.filename.split('.')[1] not in ['png', 'jpg', 'jpeg', 'bmp', 'gif']:
            return Response.failed(msg='图片格式错误')
        url = QiniuService.upload_img(file.read())
    return Response.success(url)


@article_bp.route('/upload/doc', methods=['POST'])
@login_required
def upload_doc():
    args = request.json
    doc = args.get('doc')
    id = args.get('id')
    title = args.get('name')
    assert doc is not None and len(doc) > 0
    return Response.success(ArticleService.save(g.user.name, id, title, doc))


@article_bp.route('/list', methods=['GET'])
@login_required
@log_this
def article_list():
    is_published = request.args.get('is_published') == 'true'
    return Response.success(ArticleService.article_list(g.user.name, is_published))


@article_bp.route('/detail', methods=['GET'])
@login_required
@log_this
def article_detail():
    id = request.args.get('id')
    assert id is not None
    return Response.success(ArticleService.article_detail(id, g.user.name))


@article_bp.route('/publish', methods=['POST'])
@login_required
def publish_article():
    args = request.json
    id = args.get('id')
    title = args.get('title')
    tags = args.get('tags')
    is_published = args.get('is_published')
    assert id is not None
    assert title is not None
    assert tags is not None
    return Response.success(ArticleService.publish_article(g.user.name, id, title, tags, is_published))


@article_bp.route('/like', methods=['POST'])
@login_required
def like_article():
    args = request.json
    article_id = args.get('article_id')
    user_name = g.user.name
    assert article_id is not None
    return Response.success(ArticleService.like_article(article_id, user_name))
