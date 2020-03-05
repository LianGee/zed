#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : weekly_service.py
# @Author: zaoshu
# @Date  : 2020-03-03
# @Desc  :
from model.weekly_planner import WeeklyPlanner
from model.weekly_task import WeeklyTask


class WeeklyService:

    @classmethod
    def save_planner(cls, id, user_name, workspace_id, title):
        if id is not None:
            planner = WeeklyPlanner.select().get(id)
            planner.workspace_id = workspace_id
            planner.title = title
            planner.update()
            return id
        else:
            planner = WeeklyPlanner(
                user_name=user_name,
                workspace_id=workspace_id,
                title=title
            )
            planner.insert()
            return WeeklyPlanner.select().filter(
                WeeklyPlanner.user_name == user_name,
                WeeklyPlanner.title == title,
                WeeklyPlanner.workspace_id == workspace_id
            ).first().id

    @classmethod
    def save_task(cls, user_name, task):
        id = task.get('id')
        if id is not None:
            weekly_task = WeeklyTask.select().get(id)
            weekly_task.content = task.get('content')
            weekly_task.status = task.get('status')
            weekly_task.start = task.get('start')
            weekly_task.end = task.get('end')
            weekly_task.update()
            return id
        else:
            weekly_task = WeeklyTask(
                planner_id=task.get('planner_id'),
                task_index=task.get('task_index'),
                user_name=user_name,
                content=task.get('content')
            )
            weekly_task.insert()
        return WeeklyTask.select().filter(
            WeeklyTask.planner_id == task.get('planner_id'),
            WeeklyTask.user_name == user_name,
            WeeklyTask.content == task.get('content')
        ).first().id

    @classmethod
    def task_list(cls, user_name, planner_id):
        tasks = WeeklyTask.select().filter(
            WeeklyTask.user_name == user_name,
            WeeklyTask.planner_id == planner_id
        ).all()
        results = [[], [], [], [], [], [], []]
        for task in tasks:
            result = results[task.task_index]
            if len(result) == 0:
                results[task.task_index] = [task.get_json()]
            else:
                results[task.task_index].append(task.get_json())
        return results
