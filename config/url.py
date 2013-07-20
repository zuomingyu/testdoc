#!/usr/bin/env python
# coding: utf-8

pre_fix = 'controllers.'

##URL匹配可以使用正则
urls = (
        
    '^/$',                                          'redirect /selenium', 
    '^/404page$',                                   'redirect /selenium/404', 
    '^/selenium/?$',                               'redirect /selenium/doc/index', 
    '^/selenium/doc/([^/]+)$',                          pre_fix + 'selenium.doc',
    '^/selenium/([^/]+)/?$',                        pre_fix + 'selenium.index',  
    '^/pythonapi/$',                               'redirect /pythonapi/index',  
    '^/pythonapi/([^/]+)$',                        pre_fix + 'pythonapi', 
    
)
