#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : weekly_task.py
# @Author: zaoshu
# @Date  : 2020-03-03
# @Desc  :
import math
from datetime import datetime

from sqlalchemy import Column, String, Text, Integer, BigInteger

from model.base import BaseModel
from model.db import Model


class WeeklyTask(Model, BaseModel):
    __tablename__ = 'weekly_task'

    planner_id = Column(BigInteger)
    task_index = Column(Integer)
    user_name = Column(String)
    content = Column(Text)
    status = Column(Integer, default=0)
    start = Column(BigInteger, index=True, default=math.floor(datetime.now().timestamp()))
    end = Column(BigInteger, index=True, default=math.floor(datetime.now().timestamp()))
