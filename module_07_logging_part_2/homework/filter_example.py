import logging


class CustomFilter(logging.Filter):

    def filter(self, record):
        return record.msg.isascii()


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
)

logger = logging.getLogger(__name__)
logger.addFilter(CustomFilter())

if __name__ == '__main__':
    logger.info("String initialization with ASCII characters")
    logger.info("Инициализация строки с ASCI символами")
    logger.info("Инициализация строки с ASCI символами. String initialization with ASCII characters")
    logger.info("Initialization ASCII characters")