#!/usr/bin/env python
# coding: utf-8
#import web
from config import settings
from tools.lang import analysis_module_file

render = settings.selenium_render
#db = settings.db
content_dict = { 
                'page_title' : 'Selenium 中文文档', 
                
                'previous_link' : '#', 
                'previous_title' : 'Selenium 背景介绍',
                
                'next_link' : '#',
                'next_title' : 'Selenium IDE使用',   
                
                'context' : '文章目录占位符',
                
                'content' : '<h3>文本内容占位符</h3>',                        
                }
class index:
    def GET(self, page_name):
#        content_dict = analysis_module_file('index.cn')
        return render.selenium_base(content_dict)
    
class note_to_user:
    def GET(self, page_name):
#        content_dict = analysis_module_file('00_note.cn')
        return render.selenium_base(content_dict)
    
class introducing_selenium:
    def GET(self, page_name):
#        content_dict = analysis_module_file('01_introducing_selenium.cn')
        return render.selenium_base(content_dict)    
    
class selenium_ide:
    def GET(self, page_name):
#        content_dict = analysis_module_file('02_selenium_ide.cn')
        return render.selenium_base(content_dict) 

class webdriver:
    def GET(self, page_name):
#        content_dict = analysis_module_file('03_webdriver.cn')
        return render.selenium_base(content_dict)
    
class webdriver_advanced:
    def GET(self, page_name):
#        content_dict = analysis_module_file('04_webdriver_advanced.cn')
        return render.selenium_base(content_dict)
    
class selenium_rc:
    def GET(self, page_name):
#        content_dict = analysis_module_file('05_selenium_rc.cn')
        return render.selenium_base(content_dict)
    
class test_design_considerations:
    def GET(self, page_name):
#        content_dict = analysis_module_file('06_test_design_considerations.cn')
        return render.selenium_base(content_dict)        

class selenium_grid:
    def GET(self, page_name):
#        content_dict = analysis_module_file('07_selenium_grid.cn')
        return render.selenium_base(content_dict)
    
class user_extensions:
    def GET(self, page_name):
#        content_dict = analysis_module_file('08_user_extensions.cn')
        return render.selenium_base(content_dict)

class cheat_sheet:
    def GET(self, page_name):
#        content_dict = analysis_module_file('09_cheat_sheet.cn')
        return render.selenium_base(content_dict)
    
class installing_android_driver:
    def GET(self, page_name):
#        content_dict = analysis_module_file('10_installing_android_driver.cn')
        return render.selenium_base(content_dict)
    
class installing_dotnet_driver_client:
    def GET(self, page_name):
#        content_dict = analysis_module_file('11_installing_dotnet_driver_client.cn')
        return render.selenium_base(content_dict)
    
        
class installing_java_driver_Sel20_via_maven:
    def GET(self, page_name):
#        content_dict = analysis_module_file('12_installing_java_driver_Sel20_via_maven.cn')
        return render.selenium_base(content_dict)  
    
class installing_java_driver_client:
    def GET(self, page_name):
#        content_dict = analysis_module_file('13_installing_java_driver_client.cn')
        return render.selenium_base(content_dict)  

class installing_python_driver_client:
    def GET(self, page_name):
#        content_dict = analysis_module_file('14_installing_python_driver_client.cn')
        return render.selenium_base(content_dict)  
    
class locating_techniques:
    def GET(self, page_name):
#        content_dict = analysis_module_file('15_locating_techniques.cn')
        return render.selenium_base(content_dict) 
    
class migrating_from_rc_to_webdriver:
    def GET(self, page_name):
#        content_dict = analysis_module_file('16_migrating_from_rc_to_webdriver.cn')
        return render.selenium_base(content_dict) 
                          
