#!/usr/bin/env python
# coding: utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

f = open(r'C:\Documents and Settings\chenxiaowu\My Documents\GitHub\testdoc\langfiles\ReadMe', 'r')
browser = webdriver.Chrome() # Get local session of firefox
for l in f:
    k_v = l.split(' :', 1)
    browser.get(k_v[1]) # Load page
    #elem = browser.find_elements_by_class_name("c")
    elem = browser.find_elements_by_xpath("//div[@class='sphinxsidebarwrapper']/ul")
    #elem = browser.find_elements_by_css_selector("div.sphinxsidebarwrapper ul")
    if elem:
        elem = elem[0]
        source_code = elem.get_attribute("outerHTML")
        f = open('D:/%s' % k_v[0].strip(), 'w')
        f.write(source_code.encode('utf-8'))
        f.close()
        time.sleep(0.2) 

browser.close()