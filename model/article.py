#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : article.py
# @Author: zaoshu
# @Date  : 2020-02-13
# @Desc  :
from sqlalchemy import Column, String, Boolean, BigInteger

from model.base import BaseModel
from model.db import Model


class Article(Model, BaseModel):
    __tablename__ = 'article'
    catalogue_id = Column(BigInteger, default=1)
    catalogue_index = Column(BigInteger, default=0)
    title = Column(String)
    user_name = Column(String)
    file_key = Column(String)
    url = Column(String)
    is_published = Column(Boolean, default=False)
    tags = Column(String, default='[]')
    summary = Column(String)
    view_num = Column(BigInteger, default=0)
    like_num = Column(BigInteger, default=0)
    comment_num = Column(BigInteger, default=0)
