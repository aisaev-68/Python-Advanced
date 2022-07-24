import logging
import sys

from flask import Flask
from typing import Tuple

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def home() -> str:
    logging.info("Hello world log")
    return "Hello, World!"


@app.route("/one")
def one() -> Tuple[str, int]:
    logging.info("Created log")
    return "Created", 201


@app.route("/two")
def two() -> Tuple[str, int]:
    logging.info("Accepted log")
    return "Accepted", 202


@app.route("/three")
def three() -> Tuple[str, int]:
    logging.info("Non-Authoritative Information log")
    return "Non-Authoritative Information", 203


@app.route("/four")
def four() -> Tuple[str, int]:
    logging.info("No Content log")
    return "No Content", 204


@app.route("/five")
def five() -> Tuple[str, int]:
    logging.info("Reset Content")
    return "Reset Content", 205


@app.route("/error")
def error_handler() -> Tuple[str, int]:
    a = 1 / 0
    logging.error(f'error: {sys.exc_info()}')
    return "error", 500



if __name__ == "__main__":
    app.run(host="0.0.0.0")
