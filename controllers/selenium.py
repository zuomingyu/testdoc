#!/usr/bin/env python
# coding: utf-8
import web
from config import settings
from tools.lang import analysis_module_file

render = settings.selenium_render
#db = settings.db
#content_dict = { 
#                'page_title' : 'Selenium 中文文档', 
#                
#                'previous_link' : '#', 
#                'previous_title' : 'Selenium 背景介绍',
#                
#                'next_link' : '#',
#                'next_title' : 'Selenium IDE使用',   
#                
#                'context' : '文章目录占位符',
#                
#                'content' : '<h3>文本内容占位符</h3>',                        
#                }

class doc:
    def GET(self, page_name):
        content_dict = analysis_module_file(page_name)
        if content_dict:
            return render.selenium_doc(content_dict)
        else:
            return web.seeother("/404page")  ##redirect to 404 Page

class index:
    def GET(self, arg):
        if arg in ['cookbook', 'cookbook/']:
            return render.selenium_book({'page_title':"Cookbook For Selenium"})                        
        elif arg in ['tutorials', 'tutorials/']:
            return render.selenium_book({'page_title':"Tutorials For Selenium"})
        elif arg in ['404', '404/']:
            return render.selenium_book({'page_title':"404 Page Not Found!"})        
        else:
            web.seeother("/404page")
            
