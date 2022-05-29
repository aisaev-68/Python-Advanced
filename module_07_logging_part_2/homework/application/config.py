import logging


class HandleToDifferentFiles(logging.Handler):
    def __init__(self, filename: str, mode: str = 'a'):
        super().__init__()
        self.file = filename
        self.mode = mode

    def emit(self, record: logging.LogRecord) -> None:
        message = self.format(record) + '\n'
        if record.levelname == 'DEBUG':
            with open(f'dedug-{self.file}', mode=self.mode) as f:
                f.write(message)
        if record.levelname == 'INFO':
            with open(f'info-{self.file}', mode=self.mode) as f:
                f.write(message)
        if record.levelname == 'WARNING':
            with open(f'warning-{self.file}', mode=self.mode) as f:
                f.write(message)
        if record.levelname == 'ERROR':
            with open(f'error-{self.file}', mode=self.mode) as f:
                f.write(message)


logging_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'loggers': {
        'app': {
            'level': 'DEBUG',
            'handlers': ['console_handler', 'file_handler'],
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
        'file_handler': {
            '()': HandleToDifferentFiles,
            'level': 'DEBUG',
            'formatter': 'formatter',
            'filename': 'app.log',
            'mode': 'a',
        },
    },
    'formatters': {
        'formatter': {
            'format': '%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S%Z'
        },
    },

}
