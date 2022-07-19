from flask import Flask
from loguru import logger
from typing import Tuple

app = Flask(__name__)

logger.add(
    "logs/log.log",
    rotation='1 week',
    compression='zip',
    level='INFO',
    format="{time} {level} {message}",
    backtrace=True,
    diagnose=True
)


@app.route('/one')
def one() -> Tuple[str, int]:
    logger.info('one route')
    return 'one', 200


@app.route('/error')
def error() -> Tuple[str, int]:
    try:
        null_var = 0
        a = 1 / null_var
    except ZeroDivisionError:
        logger.exception("Error")
    return 'error', 500


@app.route('/decorator_error')
@logger.catch
def decorator_error() -> Tuple[str, int]:
    null_var = 0
    a = 1 / null_var
    return 'decorator_error', 500


if __name__ == '__main__':
    app.run()
