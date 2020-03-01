#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : graph.py
# @Author: zaoshu
# @Date  : 2020-02-15
# @Desc  :
from flask import Blueprint, request, g

from common.login import login_required
from common.response import Response
from service.graph_service import GraphService

graph_bp = Blueprint('graph', __name__)


@graph_bp.route('/share/img', methods=['GET'])
@login_required
def share_img():
    id = request.args.get('id')
    user_name = g.user.name
    assert id is not None
    return Response.success(GraphService.get_share_img(user_name, id))


@graph_bp.route('/save', methods=['POST'])
@login_required
def save():
    user_name = g.user.name
    id = request.json.get('id')
    data = request.json.get('data')
    title = request.json.get('name')
    img = request.json.get('img')
    type = request.json.get('type')
    assert data is not None
    assert type is not None
    assert img is not None
    return Response.success(GraphService.save_graph(user_name, id, type, title, data, img))


@graph_bp.route('/query', methods=['GET'])
@login_required
def query():
    id = request.args.get('id')
    assert id is not None
    return Response.success(GraphService.query(id))


@graph_bp.route('/list', methods=['POST'])
@login_required
def graph_list():
    type = request.json.get('type')
    is_published = request.json.get('isPublished')
    assert type is not None
    assert is_published is not None
    return Response.success(GraphService.graph_list(g.user.name, type, is_published))


@graph_bp.route('/delete', methods=['DELETE'])
@login_required
def delete_graph():
    id = request.args.get('id')
    assert id is not None
    return Response.success(GraphService.delete(g.user.name, id))


@graph_bp.route('/album/upload/image', methods=['POST'])
@login_required
def upload_image():
    files = request.files
    file = files.get('file')
    album_id = request.form.get('album_id')
    assert album_id is not None
    assert file is not None
    return Response.success(GraphService.upload_image(g.user.name, album_id, file))


@graph_bp.route('/image/list', methods=['GET'])
@login_required
def image_list():
    album_id = request.args.get('album_id')
    user_name = g.user.name
    return Response.success(GraphService.image_list(user_name, album_id))


@graph_bp.route('/image/delete', methods=['DELETE'])
@login_required
def delete_image():
    id = request.args.get('id')
    return Response.success(GraphService.delete_image(g.user.name, id))
