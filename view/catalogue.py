#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : catalogue.py
# @Author: zaoshu
# @Date  : 2020-02-23
# @Desc  :
from flask import Blueprint, request, g

from common.login import login_required
from common.response import Response
from model.catalogue import Catalogue
from service.catalogue_service import CatalogueService

catalogue_bp = Blueprint('catalogue', __name__)


@catalogue_bp.route('/save', methods=['POST'])
@login_required
def save():
    return Response.success(CatalogueService.save(g.user.name, request.json))


@catalogue_bp.route('/delete', methods=['DELETE'])
@login_required
def delete():
    id = request.args.get('id')
    return Response.success(CatalogueService.delete(id))


@catalogue_bp.route('/get', methods=['GET'])
@login_required
def get_catalogue():
    return Response.success(CatalogueService.get_catalogue(g.user.name))


@catalogue_bp.route('/move', methods=['POST'])
@login_required
def move_catalogue():
    src = request.json.get('src')
    des = request.json.get('des')
    return Response.success(CatalogueService.move(g.user.name, src, des))
