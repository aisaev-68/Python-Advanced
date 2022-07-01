from typing import Union, Tuple

from flask import Flask
from flask_jsonrpc import JSONRPC
from wsgiref.simple_server import WSGIRequestHandler

from flasgger import Swagger

app = Flask(__name__)

jsonrpc = JSONRPC(app, "/api", enable_web_browsable_api=True)


@jsonrpc.method("App.calculation")
def calculation(first_numb: Union[int, float], sec_numb: Union[int, float], action: str) -> Tuple[
    Union[str, float], int]:
    """
    This is an endpoint for calculating of two numbers.
    ---
    """

    if action == '+':
        return first_numb + sec_numb, 200
    elif action == '/':
        try:
            c = first_numb / sec_numb
            return c, 200
        except ZeroDivisionError as err:
            return f'{err}', 400
    elif action == '*':
        return first_numb * sec_numb, 200
    elif action == '-':
        return first_numb - sec_numb, 200


swagger = Swagger(app, template_file='schemas.json')

if __name__ == '__main__':
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(host='0.0.0.0', debug=True)
