from flask import Flask
import logging
from typing import Tuple

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route("/")
def hello_world() -> str:
    logging.info("Hello world log")
    return "Hello, World!"


@app.route("/error")
def error_handler() -> Tuple[str, int]:
    a = 1 / 0
    return "error", 500


if __name__ == "__main__":
    app.run(host='0.0.0.0')
