#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : user_like.py
# @Author: zaoshu
# @Date  : 2020-02-13
# @Desc  :
from sqlalchemy import Column, String, BigInteger, Boolean

from model.base import BaseModel
from model.db import Model


class UserLike(Model, BaseModel):
    __tablename__ = 'user_like'
    user_name = Column(String)
    article_id = Column(BigInteger)
    comment_id = Column(BigInteger)
    liked = Column(Boolean, default=False)
