"""
Логов бывает очень много. А иногда - ооооооооочень много.
Из-за этого люди часто пишут логи не в человекочитаемом,
    а в машиночитаемом формате, чтобы машиной их было обрабатывать быстрее.

Напишите функцию

def log(level: str, message: str) -> None:
    pass


которая будет писать лог  в файл skillbox_json_messages.log в следующем формате:
{"time": "<время>", "level": "<level>", "message": "<message>"}

сообщения должны быть отделены друг от друга символами переноса строки.
Обратите внимание: наше залогированное сообщение должно быть валидной json строкой.

Как это сделать? Возможно метод json.dumps поможет вам?
"""

import json
import time


def log(level: str, message: str) -> None:
    with open('skillbox_json_messages.log', 'a', encoding='utf-8') as file:
        loc_time = time.strftime('%H:%M:%S %p', time.localtime())
        data = json.dumps({"time": f'{loc_time}', "level": f'{level}', "message": f'{message}'}, ensure_ascii=False)
        print(data)
        file.write(f'{data}\n')


if __name__ == "__main__":
    log('password_checker', 'Вы пытаетесь аутентифицироваться в Skillbox')
