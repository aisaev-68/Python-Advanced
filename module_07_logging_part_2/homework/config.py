import logging
from logging.config import dictConfig

logging_config = {
    'version': 1,
    'loggers': {
        'app_log': {  # root logger
            'level': 'DEBUG',
            'handlers': ['applog'],
        },
        'stdout': {
            'level': 'DEBUG',
            'propagate': False,
            'handlers': ['stdout'],
        },
    },
    'handlers': {
        'applog': {
            'level': 'DEBUG',
            'formatter': 'applog',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        },
        'stdout': {
            'level': 'DEBUG',
            'formatter': 'stdout',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        },

    },
    'formatters': {
        'applog': {
            'format': '%(asctime)s.%(msecs)d %(process)s %(levelname)s %(message)s',
            'datefmt': '%Y-%m-%dT%H:%M:%S%Z'
        },
        'stdout': {
            'format': '%(asctime)s: (%(levelname)s) %(message)s',
            'datefmt': '%Y-%m-%dT%H:%M:%S%Z'
        },
    },

}

dictConfig(logging_config)

logger1 = logging.getLogger('app_log')
logger1.debug('TEST APP_LOG')

logger2 = logging.getLogger('app_log.stdout')
logger2.debug('TEST ROOT STDOUT')

logger3 = logging.getLogger('stdout')
logger3.debug('TEST STDOUT')