import json

from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException


url_map = Map([Rule('/hello/<username>', endpoint='hello_user'),
               Rule('/hello', endpoint='hello')])


def application(environ, start_response):
    urls = url_map.bind_to_environ(environ)
    status = 'OK 200'
    response_headers = [('Content-type', 'text/plain')]
    try:
        endpoint, args = urls.match()
        print(args)
    except HTTPException:
        start_response('404 Not Found', response_headers)
        return [b'Not found']

    start_response(status, response_headers)
    if endpoint == 'hello':
        response = {
            'message': 'Hello',
            'name': 'username'
        }
        return [str(response).encode()]

    elif endpoint == 'hello_user':
        response = {
            'message': 'Hello',
            'name': f'{args["username"]}'
        }
        return [str(response).encode()]

    else:
        start_response('404 Not Found', response_headers)
        return [b'Not found']