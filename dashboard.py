#! /usr/bin/env python
import config
from cgi import escape

html = open("main.html","r")
htmlstr = html.read()
html.close()

def respond(env, start_response):
    
    fragment = "<h1 class='page-header'>Dashboard</h1><img src='http://192.168.1.3:8090/' width='960' height='1280' >"

    response_body = htmlstr % { 
        'substitute': fragment 
    }
    
    strlen = str(len(response_body))
    
    # Now content type is text/html
    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', strlen)
    ]

    start_response('200 OK', response_headers)
    
    return [response_body]