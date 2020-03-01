#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : graph_service.py
# @Author: zaoshu
# @Date  : 2020-02-16
# @Desc  :
import json
from datetime import datetime

import config
from common.enc_util import md5
from common.exception import ServerException
from model.album import Album
from model.graph import Graph
from model.image import Image
from model.user import User
from service.qiniu_service import QiniuService


class GraphService:

    @classmethod
    def get_share_img(cls, user_name, id):
        graph = Graph.select().get(id)
        if graph is None:
            raise ServerException(msg='图片不存在')
        if not graph.is_published and user_name != graph.user_name:
            raise ServerException(msg='该图未发布')
        return graph

    @classmethod
    def save_graph(cls, user_name, id, type, title, data, img):
        if data:
            data = json.dumps(data)
        if title is None:
            title = 'Untitled'
        if id is not None:
            graph: Graph = Graph.select().get(id)
            graph.type = type
            graph.title = title
            data_key = md5(title + data)
            if graph.data_key != data_key:
                data_url = QiniuService.upload_doc(data, graph.data_key, data_key)
                graph.data_key = data_key
                graph.data_url = data_url
            img_key = md5(img)
            if graph.img_key != img_key:
                img_url = QiniuService.upload_img(img, graph.img_key, img_key)
                graph.img_key = img_key
                graph.img_url = img_url
                img_info = QiniuService.get_img_info(img_url)
                graph.width = img_info.get('width')
                graph.height = img_info.get('height')
                graph.size = img_info.get('size')
                graph.format = img_info.get('format')
                graph.color_model = img_info.get('colorModel')
            Graph.update(graph)
            return id
        else:
            data_key = md5(title + data + datetime.now().timestamp().__str__())
            data_url = QiniuService.upload_doc(data, file_name=data_key)
            img_key = md5(img + datetime.now().timestamp().__str__())
            img_url = QiniuService.upload_img(img, file_name=img_key)
            img_info = QiniuService.get_img_info(img_url)
            graph = Graph(
                user_name=user_name,
                title=title,
                data_key=data_key,
                data_url=data_url,
                type=type,
                img_key=img_key,
                img_url=img_url,
                width=img_info.get('width'),
                height=img_info.get('height'),
                size=img_info.get('size'),
                format=img_info.get('format'),
                color_model=img_info.get('colorModel')
            )
            graph.insert()
            return Graph.select().filter(Graph.data_key == data_key).one().id

    @classmethod
    def delete(cls, user_name, id):
        graph = Graph.select().get(id)
        assert graph is not None
        assert graph.user_name == user_name
        assert QiniuService.delete_file(bucket_name=config.QI_NIU.get('doc_bucket_name'), file_name=graph.data_key)
        assert QiniuService.delete_file(bucket_name=config.QI_NIU.get('img_bucket_name'), file_name=graph.img_key)
        graph.delete()
        return True

    @classmethod
    def query(cls, id):
        graph = Graph.select().get(id)
        data = QiniuService.get_doc(graph.data_url)
        graph_data = json.loads(data)
        result = graph.get_json()
        result['graph_data'] = graph_data
        return result

    @classmethod
    def graph_list(cls, user_name, type, is_published=True):
        if is_published:
            graphs = Graph.select().filter(Graph.type == type, Graph.is_published).order_by(
                Graph.created_at.desc()).all()
        else:
            graphs = Graph.select().filter(Graph.type == type, Graph.user_name == user_name).order_by(
                Graph.created_at.desc()).all()
        return [graph.get_json() for graph in graphs]

    @classmethod
    def image_list(cls, user_name, album_id):
        album = Album.select().get(album_id)
        if album.is_public or album.user_name == user_name:
            return Image.select().filter(Image.album_id == album_id).all()
        return []

    @classmethod
    def delete_image(cls, user_name, id):
        image = Image.select().get(id)
        delete_status = QiniuService.delete_file(config.QI_NIU.get('img_bucket_name'), image.key)
        if not delete_status:
            raise ServerException('删除图片失败')
        image.delete()
        return True
