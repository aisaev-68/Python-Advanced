import logging
from logging.config import dictConfig
import sys
from config import logging_config
from utils import string_to_operator

# logging.basicConfig(level='DEBUG')
# logger = logging.getLogger('app')
# console_handler = logging.StreamHandler(sys.stdout)
# file_handler = HandleToDifferentFiles('app.log', mode='a')
# formatter = logging.Formatter(fmt="%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s")
# file_handler.setFormatter(formatter)
# console_handler.setFormatter(formatter)
# logger.addHandler(console_handler)
# logger.addHandler(file_handler)

dictConfig(logging_config)
logger = logging.getLogger('app')


def calc(args):
    logger.info(f"Arguments: {args}")
    num_1 = args[0]
    operator = args[1]
    num_2 = args[2]

    try:
        num_1 = float(num_1)
    except ValueError as e:
        logger.error("Error while converting number 1", exc_info=True)
        logger.debug(e.args[0])

    try:
        num_2 = float(num_2)
    except ValueError as e:
        logger.error("Error while converting number 2", exc_info=True)
        logger.debug(e.args[0])

    operator_func = string_to_operator(operator)
    try:
        result = operator_func(num_1, num_2)
        logger.info(f"Result: {result}")
        logger.info(f"{num_1} {operator} {num_2} = {result}")
    except Exception as err:
        logger.exception(err)




if __name__ == '__main__':
    logger.info('Start programm')
    calc(sys.argv[1:])
