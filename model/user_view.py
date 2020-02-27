#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : user_view.py
# @Author: zaoshu
# @Date  : 2020-02-14
# @Desc  :
from sqlalchemy import Column, String, BigInteger

from model.base import BaseModel
from model.db import Model


class UserView(Model, BaseModel):
    __tablename__ = 'user_view'
    user_name = Column(String)
    article_id = Column(BigInteger)
