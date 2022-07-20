import random
import time

from flask import Flask

from typing import Tuple

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route('/one')
def first_route():
    time.sleep(random.random() * 0.2)
    return 201


@app.route('/two')
def the_second():
    time.sleep(random.random() * 0.4)
    return 202


@app.route('/three')
def test_3rd():
    time.sleep(random.random() * 0.6)
    return 203


@app.route('/four')
def fourth_four():
    time.sleep(random.random() * 0.8)
    return 204

@app.route('/five')
def fourth_five():
    time.sleep(random.random() * 0.8)
    return 205

@app.route("/error")
def error_handler() -> Tuple[str, int]:
    a = 1 / 0
    return "error", 500


if __name__ == "__main__":
    app.run(host='0.0.0.0')
