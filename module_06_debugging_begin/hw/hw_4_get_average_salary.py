"""
Вы работаете программистом на предприятии.
К вам пришли из бухгалтерии и попросили посчитать среднюю зарплату по предприятию.
Вы посчитали, получилось слишком много, совсем не реалистично.
Вы подумали и проконсультировались со знакомым из отдела статистики.
Он посоветовал отбросить максимальную и минимальную зарплату.
Вы прикинули, получилось что-то похожее на правду.

Реализуйте функцию get_average_salary_corrected,
которая принимает на вход непустой массив заработных плат
(каждая -- число int) и возвращает среднюю з/п из этого массива
после отбрасывания минимальной и максимальной з/п.

Задачу нужно решить с алгоритмической сложностью O(N) , где N -- длина массива зарплат.

Покройте функцию логгированием.
"""
import logging
import random
from typing import List

logger = logging.getLogger("password_checker")
logging.basicConfig(filename='out.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(name)s - %(message)s', datefmt='%I:%M:%S %p')


def get_average_salary_corrected(salaries: List[int]) -> float:
    min_numb = min(salaries)
    max_numb = max(salaries)
    logger.info('Старт выполнения функции')
    lst = [i for i in salaries if min_numb < i < max_numb]
    logger.info('Завершение выполнения функции')
    return sum(lst) / len(lst)


if __name__ == "__main__":
    list_salaries = random.choices([i for i in range(15000, 95000, 5000)], k=1000000)
    print('Средняя заработная плата: ', get_average_salary_corrected(list_salaries))
