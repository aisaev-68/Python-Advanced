"""
В своей работе программист должен часто уметь решать рутинные задачи.

Хорошим примером такой задачи является вычисление суммарного размера директории.

Пожалуйста реализуйте функцию, которая на вход принимает путь до папки
    в виде стрки или объекта Path
и возвращает суммарный объём директории в байтах.

В случае, если на вход функции передаётся несуществующий путь или НЕ директория,
    функция должна выкинуть исключение ValueError с красивым описание ошибки
"""

from pathlib import Path
from typing import Union


def calculate_directory_size(directory_path: Union[str, Path] = ".") -> int:
    path = Path(directory_path)
    size_file = 0

    if path.exists() and path.is_dir():
        for x in path.iterdir():
            if x.is_file():
                size_file += x.stat().st_size
    else:
        raise ValueError('Не существующий путь или директория')

    return size_file


if __name__ == "__main__":
    input_path1 = '/home/aisaev/python_advanced/module_08_deploy/hw'
    input_path2 = 'hw_2_create_new_user.md'
    print(f'Объём директории {input_path1} в байтах:', calculate_directory_size(input_path1))
    print(f'Объём директории {input_path2} в байтах:', calculate_directory_size(input_path2))
