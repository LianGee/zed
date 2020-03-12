#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : socket.py
# @Author: zaoshu
# @Date  : 2020-03-12
# @Desc  :
import json

from flask import Blueprint

socket_bp = Blueprint(r'socket', __name__)


@socket_bp.route('/game')
def draw(socket):
    # draw_sockets.append(draw_sockets)
    while not socket.closed:
        message = socket.receive()
        data = json.loads(message)
        chat = data.get('chat', [])
        if isinstance(data.get('chat'), list) and len(chat) > 50:
            data['chat'] = chat[0: 50]
        for client in socket.handler.server.clients.values():
            client.ws.send(json.dumps(data))
