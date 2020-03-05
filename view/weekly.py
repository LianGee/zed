#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : weekly.py
# @Author: zaoshu
# @Date  : 2020-03-04
# @Desc  :
from flask import Blueprint, request, g

from common.loged import log_this
from common.login import login_required
from common.response import Response
from service.weekly_service import WeeklyService

weekly_bp = Blueprint('weekly', __name__)


@weekly_bp.route('/planner/save', methods=['post'])
@login_required
@log_this
def save_planner():
    id = request.json.get('id')
    workspace_id = request.json.get('workspace_id')
    title = request.json.get('title')
    user_name = g.user.name
    return Response.success(WeeklyService.save_planner(
        user_name=user_name,
        id=id,
        workspace_id=workspace_id,
        title=title
    ))


@weekly_bp.route('/task/list', methods=['GET'])
@login_required
@log_this
def get_task_list():
    planner_id = request.args.get('id')
    user_name = g.user.name
    return Response.success(WeeklyService.task_list(user_name, planner_id))


@weekly_bp.route('/task/save', methods=['post'])
@login_required
@log_this
def save_task():
    task = request.json
    user_name = g.user.name
    return Response.success(WeeklyService.save_task(user_name, task))
