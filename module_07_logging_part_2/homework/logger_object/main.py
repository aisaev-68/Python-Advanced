import logging
from logging.config import dictConfig

import flask

from http_utils import get_ip_address
from subprocess_utils import get_kernel_version
import logging_tree
from logging_tree import printout

logging_config = {
    'version': 1,
    'disable_existing_loggers': True,
    'loggers': {
        'main.py': {
            'level': 'DEBUG',
            'handlers': ['file_handler'],
            'propagate': False,
        },
        'subprocess_utils': {
            'level': 'DEBUG',
            'propagate': False,
            'handlers': ['file_handler'],
        },
        'http_utils': {
            'level': 'INFO',
            'handlers': ['file_handler'],
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'level': 'INFO',
            'formatter': 'formatter',
            'filename': 'logconfig.log',
            'when': 'h',
            'interval': 10,
        },

    },
    'formatters': {
        'formatter': {
            'format': '%(process)s | %(levelname)s | %(asctime)s | %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S%Z'
        },
    },

}


dictConfig(logging_config)
logger = logging.getLogger('main.py')

app = flask.Flask(__name__)


@app.route('/get_system_info')
def get_system_info():
    logger.info('Start working')
    ip = get_ip_address()
    kernel = get_kernel_version()
    with open('log_tree.txt', 'w', encoding='utf-8') as file:
        file.write(logging_tree.format.build_description())
    return "<p>{}</p><p>{}</p>".format(ip, kernel)


if __name__ == '__main__':
    app.run(debug=True)

