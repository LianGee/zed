#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : album.py
# @Author: zaoshu
# @Date  : 2020-02-28
# @Desc  :
from flask import Blueprint, request, g

from common.login import login_required
from common.response import Response
from service.album_service import AlbumService

album_bp = Blueprint('album', __name__)


@album_bp.route('/list', methods=['GET'])
@login_required
def get_album_list():
    user_name = g.user.name
    is_public = request.args.get('is_public') == 'true'
    return Response.success(AlbumService.album_list(user_name, is_public))


@album_bp.route('/img/list', methods=['GET'])
@login_required
def get_img_list():
    album_id = request.args.get('album_id')
    user_name = g.user.name
    return Response.success(AlbumService.img_list(user_name, album_id))


@album_bp.route('/public', methods=['POST'])
@login_required
def public_album():
    id = request.json.get('id')
    assert id is not None
    return Response.success(AlbumService.public_album(id))


@album_bp.route('/save', methods=['POST'])
@login_required
def save():
    user_name = g.user.name
    id = request.json.get('id')
    title = request.json.get('title')
    description = request.json.get('description')
    cover_url = request.json.get('cover_url')
    assert user_name is not None
    return Response.success(AlbumService.create_album(
        user_name=user_name,
        id=id,
        title=title,
        description=description,
        cover_url=cover_url
    ))


@album_bp.route('/album/upload/image', methods=['POST'])
@login_required
def upload_image():
    files = request.files
    file = files.get('file')
    album_id = request.form.get('album_id')
    assert album_id is not None
    assert file is not None
    return Response.success(AlbumService.upload_image(g.user.name, album_id, file))
