#!/usr/bin/env python
# coding: utf-8
import web
from config import settings

render = settings.python_render
#db = settings.db

class index:
    def GET(self, page_name):
        return render.python_index()