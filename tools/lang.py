#!/usr/bin/env python
# coding: utf-8
import os
import web

def analysis_module_file(post_str):
    print post_str
    content_dict = { 
                'page_title' : 'Selenium 中文文档', 
                
                'previous_link' : '#', 
                'previous_title' : 'Selenium 背景介绍',
                
                'next_link' : '#',
                'next_title' : 'Selenium IDE使用',   
                
                'context' : '文章目录占位符',
                
                'content' : '<h3>文本内容占位符</h3>',                        
                }
    cn_file_name = os.path.join(web.config['work_dir'], 'langfiles', '%s.cn' % post_str)
    en_file_name = os.path.join(web.config['work_dir'], 'langfiles', '%s.en' % post_str)
    if os.path.exists(cn_file_name):
        goal_file = cn_file_name
    elif os.path.exists(en_file_name):
        goal_file = en_file_name
    else:
        return None    ##没有找到对应的文件
    t_dict = analysis_file_data(goal_file)
    if t_dict:
        return t_dict
    else:
        return content_dict
    
def analysis_file_data(file_name):
    pass
    
def read_big_file(file_name):
    with open(file_name, 'r') as f:
        yield f.readline()

        
        