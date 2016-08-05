import os
from app import create_app
from flask_migrate import upgrade
application = create_app('production')

if __name__ == '__main__':
    # from wsgiref.simple_server import make_server
    # httpd = make_server('localhost', 8080, application)
    # httpd.serve_forever()
    application.run(port=8080)
