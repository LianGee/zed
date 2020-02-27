#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : user_service.py
# @Author: zaoshu
# @Date  : 2020-02-10
# @Desc  :
import json

from flask import session
from sqlalchemy.orm.exc import NoResultFound

from common.enc_util import md5
from model.tag import Tag
from model.user import User


class UserService:

    @classmethod
    def register(cls, user: User) -> bool:
        if user.password is not None:
            user.password = md5(user.password)
        User.insert(user)
        return True

    @classmethod
    def login(cls, name: str, password: str) -> bool:
        password = md5(password)
        try:
            user = User.select().filter(User.name == name, User.password == password).one()
        except NoResultFound:
            return False
        session['user'] = json.dumps(user.get_json())
        return user is not None

    @classmethod
    def user_tag(cls, user_name):
        tags = Tag.select().filter(Tag.user_name == user_name).all()
        return [tag.get_json() for tag in tags]
