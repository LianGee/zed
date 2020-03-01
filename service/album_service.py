#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : album_service.py
# @Author: zaoshu
# @Date  : 2020-02-28
# @Desc  :
import math

import config
from common.exception import ServerException
from common.log import Logger
from model.album import Album
from model.image import Image
from model.user import User
from service.qiniu_service import QiniuService

log = Logger(__name__)


class AlbumService:

    @classmethod
    def album_list(cls, user_name, is_public=True):
        if is_public:
            albums = Album.select().filter(Album.is_public).all()
        else:
            albums = Album.select().filter(Album.user_name == user_name).all()
        user_names = [album.user_name for album in albums]
        users = User.select().filter(User.name.in_(user_names)).all()
        user_map = {}
        for user in users:
            user_map[user.name] = user
        results = []
        for album in albums:
            result = album.get_json()
            result['user'] = user_map.get(album.user_name).get_json()
            results.append(result)
        return results

    @classmethod
    def img_list(cls, user_name, album_id):
        album = Album.select().get(album_id)
        assert album is not None
        imgs = []
        if album.is_public or album.user_name == user_name:
            imgs = Image.select().filter(Image.album_id == album_id).order_by(Image.id.desc()).all()
        layout = []
        img_data = []
        row_height = [0] * 4
        for index, img in enumerate(imgs):
            img_data.append(img.get_json())
            row_num = math.floor(index / 4)
            col_num = index % 4
            log.info(f'{row_num}, {col_num}')
            layout.append({
                'x': 6 * (index % 4),
                'y': sum([lo.get('h', 0) if (i % 6) == col_num else 0 for i, lo in enumerate(layout)]),
                'w': 6,
                'h': math.floor(img.height / img.width * 9),
                'i': img.key,
                'index': index
            })
        for i in range(4):
            row_height[i] = sum([lo.get('h', 0) if index % 4 == i else 0 for index, lo in enumerate(layout)])
        return {
            'imgs': img_data,
            'layout': layout,
            'row_height': max(row_height)
        }

    @classmethod
    def delete_album(cls, id):
        album = Album.select().get(id)
        assert album is not None
        images = Image.select().filter(Image.album_id == id).all()
        for image in images:
            QiniuService.delete_file(config.QI_NIU.get('img_bucket_name'), image.key)
            image.delete()
        album.delete()
        return True

    @classmethod
    def public_album(cls, id):
        album = Album.select().get(id)
        assert album is not None
        album.is_public = not album.is_public
        album.update()
        return True

    @classmethod
    def create_album(cls, user_name, id, title, cover_url, description):
        if id is not None:
            album = Album.select().get(id)
            assert album is not None
            album.title = title
            album.cover_url = cover_url
            album.description = description
            album.update()
            return id
        else:
            existed = Album.select().filter(Album.title == title, Album.user_name == user_name).first() is not None
            if existed:
                raise ServerException(msg='相册已存在')
            album = Album(
                title=title,
                cover_url=cover_url,
                description=description,
                user_name=user_name,
            )
            album.insert()
        return Album.select().filter(Album.title == title, Album.user_name == user_name).one().id
