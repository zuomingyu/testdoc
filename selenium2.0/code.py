#!/usr/bin/env python
# coding: utf-8
from config.url import urls
import web

import sys
print sys.getdefaultencoding()
reload(sys)
sys.setdefaultencoding('utf-8') 
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
