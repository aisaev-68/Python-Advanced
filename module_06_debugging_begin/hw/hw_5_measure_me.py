"""
Обычно мы пишем логи с какой-то целью.
Иногда для дебага, иногда для своевременного реагирования на ошибки.
Однако с логами можно делать очень-очень много чего.

Например, ведь верно, что каждая строка лога содержит в себе метку времени.
Таким образом, правильно организовав логгирование,
    мы можем вести статистику -- какая функция сколько времени выполняется.
Программа, которую вы видите в файле hw_5_measure_me.py пишет логи в stdout.
Внутри неё есть функция measure_me,
в начале и конце которой пишется "Enter measure_me" и "Leave measure_me".
Из-за конфигурации - в начале каждой строки с логами указано текущее время.
Запустите эту программу, соберите логи и посчитайте
среднее время выполнения функции measure_me.
"""

import sys
import logging
import random
from datetime import datetime
from typing import List

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler(stream=sys.stdout)
file_handler = logging.FileHandler(filename='measure_me.log', mode='w', encoding='utf-8')
file_handler.setLevel(logging.INFO)
handlers = [file_handler, stream_handler]

logging.basicConfig(
    format='%(asctime)s -- %(filename)s:%(lineno)d -- %(levelname)s -- %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=handlers
)


def get_data_line(sz: int) -> List[int]:
    try:
        logger.debug("Enter get_data_line")
        return [random.randint(-(2 ** 31), 2 ** 31 - 1) for _ in range(sz)]
    finally:
        logger.debug("Leave get_data_line")


def measure_me(nums: List[int]) -> List[List[int]]:
    logger.info("Enter measure_me")
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        logger.debug(f"Iteration {i}")
        left = i + 1
        right = len(nums) - 1
        target = 0 - nums[i]
        if i == 0 or nums[i] != nums[i - 1]:
            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    logger.debug(f"Found {target}")
                    results.append([nums[i], nums[left], nums[right]])
                    logger.debug(
                        f"Appended {[nums[i], nums[left], nums[right]]} to result"
                    )
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif s < target:
                    logger.debug(f"Increment left (left, right) = {left, right}")
                    left += 1
                else:
                    logger.debug(f"Decrement right (left, right) = {left, right}")

                    right -= 1

    logger.info("Leave measure_me")

    return results


def get_lead_time(data_lst: list) -> str:
    """Функция возвращает время затраченное
    на выполнение функции measure_me
    """
    start_date_time = data_lst[0].split('--')[0].strip()
    end_date_time = data_lst[len(data_lst) - 1].split('--')[0].strip()
    time_differ = str(
        datetime.strptime(end_date_time, "%Y-%m-%d %H:%M:%S") - datetime.strptime(start_date_time, "%Y-%m-%d %H:%M:%S"))

    return time_differ


if __name__ == "__main__":
    for it in range(15):
        data_line = get_data_line(10 ** 3)
        measure_me(data_line)

    with open('measure_me.log', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print('Время затраченное на выполнение функции measure_me:', get_lead_time(data))
