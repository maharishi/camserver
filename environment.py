#! /usr/bin/env python

# Python's bundled WSGI server
from wsgiref.simple_server import make_server
import re
from cgi import escape

import cam

import dashboard

import exception

def index(environ, start_response):
    # Sorting and stringifying the environment key, value pairs
    response_body = [
        '%s: %s' % (key, value) for key, value in sorted(environ.items())
    ]
    response_body = '\n'.join(response_body)

    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]
    start_response(status, response_headers)

    return [response_body]

# map urls to functions 
urls = [
    (r'cam.py/?$', cam.respond),
    (r'^$', dashboard.respond)
]

def not_found(environ, start_response):
    """Called if no URL matches."""
    start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])
    return ['Not Found']


def application (environ, start_response):
    path = environ.get('PATH_INFO', '').lstrip('/')
    for regex, callback in urls:
        match = re.search(regex, path) 
    if match is not None:
        environ['myapp.url_args'] = match.groups()
        return callback(environ, start_response)
    return not_found(environ, start_response)

# Instantiate the server
httpd = make_server (
    'localhost', # The host name
    8051, # A port number where to wait for the request
    exception.exception_app(application) # The application object name, in this case a function
)
httpd.serve_forever() 