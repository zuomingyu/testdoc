#!/usr/bin/env python
# coding: utf-8
from config.url import urls
import web
import os

import sys
print sys.getdefaultencoding()
reload(sys)
sys.setdefaultencoding('utf-8') 
app = web.application(urls, globals())
web.config['work_dir'] = os.getcwd()

if __name__ == "__main__":
    app.run()
