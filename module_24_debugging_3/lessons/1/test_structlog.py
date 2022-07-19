from flask import Flask, request, g
import structlog
from structlog.stdlib import LoggerFactory
import logging
import sys
from typing import Tuple

logging.basicConfig(format="%(message)s",
                    stream=sys.stdout,
                    level=logging.INFO)

app = Flask(__name__)
structured_log = structlog.get_logger()

import datetime


def timestamper(_, __, event_dict):
    event_dict["time"] = datetime.datetime.now().isoformat()
    return event_dict


structlog.configure(
    processors=[timestamper, structlog.processors.JSONRenderer()],
    logger_factory=LoggerFactory())


@app.before_request
def before_request():
    method = request.method
    user_agent = request.user_agent
    log = structured_log.bind(method=method, user_agent=user_agent)
    g.log = log


@app.route('/one')
def one() -> Tuple[str, int]:
    g.log.msg('route one')
    return 'one', 200


@app.route('/two')
def two() -> Tuple[str, int]:
    g.log.msg('route two')
    return 'two', 200


if __name__ == '__main__':
    app.run()
