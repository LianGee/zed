#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : weekly_planner.py
# @Author: zaoshu
# @Date  : 2020-03-03
# @Desc  :
from sqlalchemy import Column, String, BigInteger

from model.base import BaseModel
from model.db import Model


class WeeklyPlanner(Model, BaseModel):
    __tablename__ = 'weekly_planner'
    user_name = Column(String)
    title = Column(String)
    workspace_id = Column(BigInteger)
