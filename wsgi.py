import os
from manage import manager


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 8051, manager)
    httpd.serve_forever()
