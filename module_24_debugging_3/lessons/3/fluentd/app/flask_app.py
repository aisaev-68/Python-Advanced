import time
import random
import logging
from typing import Tuple

from flask import Flask

app = Flask(__name__)
logger = logging.getLogger(__name__)
app.config['DEBUG'] = True


@app.route('/one')
def first_route() -> str:
    time.sleep(random.random() * 0.2)
    return 'ok'


@app.route('/two')
def the_second() -> str:
    time.sleep(random.random() * 0.4)
    return 'ok'


@app.route('/three')
def test_3rd() -> str:
    time.sleep(random.random() * 0.6)
    return 'ok'


@app.route('/four')
def fourth_one() -> str:
    time.sleep(random.random() * 0.8)
    return 'ok'


@app.route('/error')
def oops() -> Tuple[str, int]:
    a = 1 / 0
    return ':(', 500


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, threaded=True)
