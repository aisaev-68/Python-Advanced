import logging
import sys

from utils import string_to_operator

logger = logging.getLogger("app")
console_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(console_handler)
console_handler.setLevel(logging.DEBUG)
file_handler1 = logging.FileHandler('app_debug.log', mode='w')
file_handler1.setLevel(logging.DEBUG)
logger.addHandler(file_handler1)
file_handler2 = logging.FileHandler('app_info.log', mode='w')
file_handler2.setLevel(logging.INFO)
logger.addHandler(file_handler1)
file_handler3 = logging.FileHandler('app_warning.log', mode='w')
file_handler3.setLevel(logging.WARNING)
logger.addHandler(file_handler3)
file_handler4 = logging.FileHandler('app_critical.log', mode='w')
file_handler4.setLevel(logging.CRITICAL)
logger.addHandler(file_handler4)
formatter = logging.Formatter(fmt="%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s")
file_handler1.setFormatter(formatter)
file_handler2.setFormatter(formatter)
file_handler3.setFormatter(formatter)
file_handler4.setFormatter(formatter)
console_handler.setFormatter(formatter)



def calc(args):
    logger.info(f"Arguments: {args}")
    num_1 = args[0]
    operator = args[1]
    num_2 = args[2]

    try:
        num_1 = float(num_1)
    except ValueError as e:
        logger.exception("Error while converting number 1")
        logger.exception(e.args[0])

    try:
        num_2 = float(num_2)
    except ValueError as e:
        logger.exception("Error while converting number 2")
        logger.exception(e.args[0])

    operator_func = string_to_operator(operator)
    result = operator_func(num_1, num_2)
    logger.info(f"Result: {result}")
    logger.info(f"{num_1} {operator} {num_2} = {result}")



if __name__ == '__main__':
    calc(sys.argv[1:])
