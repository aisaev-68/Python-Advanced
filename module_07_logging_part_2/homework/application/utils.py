import logging
from typing import Union, Callable
from operator import sub, mul, truediv, add

module_logger = logging.getLogger('app.utils')

OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
}

Numeric = Union[int, float]


def string_to_operator(value: str) -> Callable[[Numeric, Numeric], Numeric]:
    """
    Convert string to arithmetic function
    :param value: basic arithmetic function
    """
    if not isinstance(value, str):
        module_logger.warning(f"wrong operator type: {value}")
        raise ValueError("wrong operator type")

    if value not in OPERATORS:
        module_logger.warning(f"wrong operator type: {value}")
        raise ValueError("wrong operator value")

    return OPERATORS[value]
