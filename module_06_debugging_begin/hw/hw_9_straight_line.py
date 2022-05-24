"""
Давайте немного отойдём от логирования.
Программист должен знать не только computer science, но и математику.
Давайте вспомним школьный курс математики.

Итак, нам нужно реализовать функцию, которая принимает на вход
list из координат точек (каждая из них - tuple с x и y).

Напишите функцию, которая определяет, лежат ли все эти точки на одной прямой или не лежат
"""

from typing import List, Tuple


def func(x, y):
    precision = 0.00077 # точность
    if y * (x_y_list[1][0] - x_y_list[0][0]) - x * (x_y_list[1][1] - x_y_list[0][1]) + \
            x_y_list[0][0] * x_y_list[1][1] - x_y_list[1][0] * x_y_list[0][1] <= precision:
        return True
    return False


def check_is_straight_line(coordinates: List[Tuple[float, float]]) -> bool:
    count = 0
    for val in coordinates:
        if func(val[0], val[1]):
            count += 1

    if len(coordinates) == count:
        return True
    return False


if __name__ == "__main__":
    x_y_list: List[Tuple[float, float]] = [(-6.5, -0.375), (-5.0, 0.0), (-2.63, 0.593), (-1.0, 1.0), (0.53, 1.383), (5.52, 2.63)]
    if check_is_straight_line(x_y_list):
        print('Точки с координатами {}\nрасположены на прямой'.format(x_y_list))
    else:
        print('Точки с координатами {}\nне расположены на прямой'.format(x_y_list))
