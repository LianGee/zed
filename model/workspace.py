#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : workspace.py
# @Author: zaoshu
# @Date  : 2020-03-04
# @Desc  :
from sqlalchemy import Column, String

from model.base import BaseModel
from model.db import Model


class Workspace(Model, BaseModel):
    __tablename__ = 'workspace'
    user_name = Column(String)
    name = Column(String)
