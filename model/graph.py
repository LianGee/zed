#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : graph.py
# @Author: zaoshu
# @Date  : 2020-02-16
# @Desc  :
from sqlalchemy import String, Integer, Boolean, Column

from model.base import BaseModel
from model.db import Model


class Graph(Model, BaseModel):
    __tablename__ = 'graph'
    title = Column(String, default='Untitled')
    type = Column(String)
    user_name = Column(String)
    data_key = Column(String)
    data_url = Column(String)
    img_key = Column(String)
    img_url = Column(String)
    width = Column(Integer)
    height = Column(Integer)
    size = Column(Integer)
    format = Column(String)
    tags = Column(String, default='[]')
    color_model = Column(String)
    is_published = Column(Boolean, default=False)
