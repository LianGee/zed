#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : tag.py
# @Author: zaoshu
# @Date  : 2020-02-23
# @Desc  :
from flask import Blueprint, g, request

from common.loged import log_this
from common.login import login_required
from common.response import Response
from service.tag_service import TagService

tag_bp = Blueprint('tag', __name__)


@tag_bp.route('/add', methods=['POST'])
@login_required
@log_this
def add_tag():
    label = request.json.get('label')
    return Response.success(TagService.add(g.user.name, label))


@tag_bp.route('/delete', methods=['DELETE'])
@login_required
@log_this
def delete_tag():
    id = request.args.get('id')
    assert id is not None
    return Response.success(TagService.delete(id))
