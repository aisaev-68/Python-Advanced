import logging
import shlex
from logging.config import dictConfig
import subprocess


logging_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'loggers': {
        'app': {
            'level': 'DEBUG',
            'handlers': ['http_handler'],
            # 'propagate': False,
        },
    },
    'handlers': {
        'console_handler': {
            'level': 'DEBUG',
            'formatter': 'formatter',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        },
        'http_handler': {
            "()": "CustomHttp",
            "level": "DEBUG",
            "formatter": "formatter",
            "host": 'http://127.0.0.1:5000',
            'url': '/',
            'method': 'GET'
        },
    },
    'formatters': {
        'formatter': {
            'format': '%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S%Z'
        },
    },
}

dictConfig(logging_config)
logger = logging.getLogger('app')


class CustomHttp(logging.Handler):
    def __init__(self, host, url, method):
        super().__init__()
        self.server = host
        self.url = url
        self.method = method

    def emit(self, record):
        message = self.format(record)
        command_str = f'curl -X {self.method} {self.server}{self.url}{message}"'
        command = shlex.split(command_str)
        subprocess.run(command)


if __name__ == '__main__':
    logger.info('Привет')
    logger.info('Пока')