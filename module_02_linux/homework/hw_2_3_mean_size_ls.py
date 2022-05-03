"""
Напишите функцию, которая будет по output команды ls возвращать средний размер файла в папке.
$ ls -l ./
В качестве аргумента функции должен выступать путь до файла с output команды ls
"""
import os


def get_mean_size(ls_output_path: str) -> float:
    file = os.path.basename(ls_output_path)
    average_size = 0
    count = 0
    with open(file, 'r') as f:
        for item in f:
            if len(item.split()) > 2:
                if item.split()[0][:1] != 'd':
                    count += 1
                    average_size += int(item.split()[4])
    return average_size / count


if __name__ == "__main__":
    ls_cmd = 'ls -l > output.txt'
    os.system(ls_cmd)
    print(f'Средний размер файла в папке', get_mean_size(os.path.join(os.getcwd(), "output.txt")))
