import logging
import sys

import flask

from http_utils import get_ip_address
from subprocess_utils import get_kernel_version


logging.basicConfig(level='DEBUG', handlers=[logging.StreamHandler(sys.stdout), logging.FileHandler(filename='1.log')])
logger = logging.getLogger('main.py')

app = flask.Flask(__name__)


@app.route('/get_system_info')
def get_system_info():
    logger.info('Start working')
    ip = get_ip_address()
    kernel = get_kernel_version()
    return "<p>{}</p><p>{}</p>".format(ip, kernel)


if __name__ == '__main__':
    app.run(debug=True)
