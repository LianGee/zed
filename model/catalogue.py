#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : catalogue.py
# @Author: zaoshu
# @Date  : 2020-02-23
# @Desc  :
from sqlalchemy import Column, String, BigInteger

from model.base import BaseModel
from model.db import Model


class Catalogue(Model, BaseModel):
    __tablename__ = 'catalogue'
    name = Column(String)
    index = Column(BigInteger, default=0)
    user_name = Column(String)
