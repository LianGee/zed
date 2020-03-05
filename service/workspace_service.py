#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : workspace_service.py
# @Author: zaoshu
# @Date  : 2020-03-04
# @Desc  :
from common.exception import ServerException
from model.weekly_planner import WeeklyPlanner
from model.workspace import Workspace


class WorkspaceService:

    @classmethod
    def save(cls, user_name, id, name):
        if id is not None:
            workspace = Workspace.select().get(id)
            workspace.name = name
            workspace.update()
            return id
        else:
            workspace = Workspace(
                user_name=user_name,
                name=name
            )
            workspace.insert()
            return Workspace.select().filter(
                Workspace.user_name == user_name,
                Workspace.name == name
            ).first().id

    @classmethod
    def list(cls, user_name):
        workspaces = Workspace.select().filter(
            Workspace.user_name == user_name
        ).order_by(Workspace.updated_at.desc()).all()
        workspace_ids = [workspace.id for workspace in workspaces]
        planners = WeeklyPlanner.select().filter(
            WeeklyPlanner.workspace_id.in_(workspace_ids)
        ).all()
        planner_map = {}
        for planner in planners:
            if planner_map.get(planner.workspace_id, None) is None:
                planner_map[planner.workspace_id] = [planner.get_json()]
            else:
                planner_map[planner.workspace_id].append(planner.get_json())
        results = []
        for workspace in workspaces:
            result = workspace.get_json()
            result['planners'] = planner_map.get(workspace.id, [])
            results.append(result)
        return results

    @classmethod
    def delete(cls, user_name, id):
        workspace = Workspace.select().get(id)
        if workspace.user_name != user_name:
            raise ServerException('无权限')
        planners = WeeklyPlanner.select().filter(WeeklyPlanner.workspace_id == id).all()
        if len(planners) != 0:
            raise ServerException('存在计划，请先删除计划')
        workspace.delete()
        return True
