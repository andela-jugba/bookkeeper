#!/usr/bin/env python
import os
from flask_migrate import upgrade
from app import create_app
application = create_app('production')

if __name__ == '__main__':
    # from wsgiref.simple_server import make_server
    # httpd = make_server('localhost', 8080, application)
    # httpd.serve_forever()
    application.run()
