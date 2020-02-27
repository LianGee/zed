#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test.py
# @Author: zaoshu
# @Date  : 2020-02-12
# @Desc  :
from flask import Blueprint, request

import config
from common.response import Response
from service.qiniu_service import QiniuService

test_bp = Blueprint('test', __name__)


@test_bp.route('/upload/img', methods=['POST'])
def upload_img():
    files = request.files
    file = files.get('file')
    url = ''
    if file is not None:
        if file.filename.split('.')[1] not in ['png', 'jpg', 'jpeg', 'bmp', 'gif']:
            return Response.failed(msg='图片格式错误')
        url = QiniuService.upload_img(file.read())
    return Response.success(url)


@test_bp.route('/upload/doc', methods=['POST'])
def upload_doc():
    args = request.json
    doc = args.get('doc')
    assert doc is not None and len(doc) > 0
    return Response.success(QiniuService.upload_doc(doc))
