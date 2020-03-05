#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : workspace.py
# @Author: zaoshu
# @Date  : 2020-03-04
# @Desc  :
from flask import Blueprint, request, g

from common.loged import log_this
from common.login import login_required
from common.response import Response
from service.workspace_service import WorkspaceService

workspace_bp = Blueprint('workspace', __name__)


@workspace_bp.route('/save', methods=['post'])
@login_required
@log_this
def save():
    id = request.json.get('id')
    name = request.json.get('name')
    user_name = g.user.name
    return Response.success(WorkspaceService.save(user_name, id, name))


@workspace_bp.route('/list', methods=['get'])
@login_required
@log_this
def get_workspace_list():
    return Response.success(WorkspaceService.list(g.user.name))


@workspace_bp.route('/delete', methods=['delete'])
@login_required
@log_this
def delete():
    id = request.args.get('id')
    user_name = g.user.name
    return Response.success(WorkspaceService.delete(user_name, id))
