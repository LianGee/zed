#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : login.py
# @Author: zaoshu
# @Date  : 2020-02-10
# @Desc  :
import functools
import json

from flask import session, g

from common.response import Response
from model.user import User


def login_required(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        login = False
        user = session.get('user')
        if user is not None:
            user = json.loads(user)
            login = user.get('name') is not None
        if not login:
            return Response.success(data='/user/login', msg='require login', status=30200)
        g.user = User.select().filter(User.name == user.get('name')).one()
        return func(*args, **kwargs)

    return wrapper
