#!/usr/bin/env python
# coding: utf-8
import web

#db = web.database(dbn='mysql', db='apiow', user='root', pw='password', charset='utf8', host="10.255.253.243")
selenium_render = web.template.render('templates/', cache=False)
python_render = web.template.render('templates/', cache=False, base='python_base')

web.config.debug = True

config = web.storage(
    email='chenxiaowu@dangdang.com',
    site_name = 'Selenium中文帮助文档',
    site_desc = '翻译selenium的官方英文文档',
    site_auther = 'XiaowuChen',    
    resources = '/static',
)

##设置为模板文件中的全局变量
web.template.Template.globals['config'] = config
web.template.Template.globals['sele_render'] = selenium_render
web.template.Template.globals['py_render'] = python_render
#web.template.Template.globals['db'] = db
#web.template.Template.globals['session'] = web.config._session

