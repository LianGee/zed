#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : tag_service.py
# @Author: zaoshu
# @Date  : 2020-02-23
# @Desc  :
from common.exception import ServerException
from model.tag import Tag


class TagService:

    @classmethod
    def add(cls, user_name, label):
        exist = Tag.select().filter(Tag.user_name == user_name, Tag.label == label).first() is None
        if not exist:
            raise ServerException(f'{label} 已存在')
        tag = Tag(
            user_name=user_name,
            label=label
        )
        tag.insert()
        return Tag.select().filter(Tag.user_name == user_name, Tag.label == label).one().id

    @classmethod
    def delete(cls, tag_id):
        tag = Tag.select().get(tag_id)
        if tag is None:
            raise ServerException('tag不存在')
        tag.delete()
        return True
