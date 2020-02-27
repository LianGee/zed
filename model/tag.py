#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : tag.py
# @Author: zaoshu
# @Date  : 2020-02-14
# @Desc  :
from sqlalchemy import Column, String

from model.base import BaseModel
from model.db import Model


class Tag(Model, BaseModel):
    __tablename__ = 'tag'
    user_name = Column(String)
    label = Column(String)
