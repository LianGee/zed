#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : image.py
# @Author: zaoshu
# @Date  : 2020-02-18
# @Desc  :
from sqlalchemy import Column, Integer, String, BigInteger, Text

from model.base import BaseModel
from model.db import Model


class Image(Model, BaseModel):
    __tablename__ = 'image'
    album_id = Column(BigInteger)
    user_name = Column(String)
    key = Column(String)
    url = Column(Text)
    size = Column(Integer)
    format = Column(String)
    width = Column(Integer)
    height = Column(Integer)
    color_model = Column(String)
