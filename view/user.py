#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : user.py
# @Author: zaoshu
# @Date  : 2020-02-10
# @Desc  :
import json

from flask import Blueprint, request, session, g

from common.log import Logger
from common.login import login_required
from common.response import Response
from model.user import User
from service.user_service import UserService

user_bp = Blueprint('user', __name__)
log = Logger(__name__)


@user_bp.route('/login', methods=['POST'])
def login():
    args = request.json
    name = args.get('userName')
    password = args.get('password')
    data = UserService.login(name, password)
    status = 'ok' if data else 'error'
    return Response.success(status=status, data=data)


@user_bp.route('/register', methods=['POST'])
def register():
    args = request.json
    user = User(
        name=args['name'],
        email=args['email'],
        password=args['password'],
    )
    return Response.success(UserService.register(user))


@user_bp.route('/current', methods=['GET'])
@login_required
def current():
    user = g.user.get_json()
    user['tags'] = UserService.user_tag(user_name=g.user.name)
    return Response.success(user)


@user_bp.route('/all', methods=['GET'])
@login_required
def query_all():
    users = User.select().all()
    return Response.success(users)


@user_bp.route('/get/authority')
def get_user_authority():
    authorities = []
    user = session.get('user')
    if user is None:
        authorities.append('guest')
    elif json.loads(user).get('name') == 'zaoshu':
        authorities.append('admin')
    else:
        authorities.append('user')
    return Response.success(authorities)


@user_bp.route('/get/info')
@login_required
def get_user_info():
    user_name = request.args.get('user_name')
    assert user_name is not None
    return Response.success(UserService.get_user_info(user_name))


@user_bp.route('/logout')
@login_required
def logout():
    session.pop('user')
    g.user = None
    return Response.success(True)
