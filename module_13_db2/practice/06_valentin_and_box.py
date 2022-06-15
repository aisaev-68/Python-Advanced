"""
Пожалуйста, запустите скрипт generate_practice_database.py прежде, чем приступать к выполнению практической работы. После выполнения скрипта у вас должен появиться файл базы practise.db
Начинающий боксёр Валентин прикинул, что, чтобы стать Чемпионом мира в своём весе ему
    надо победить 21 соперника (последний бой - с действующим держателем пояса).
    Валентин - очень целеустремлённый и составил в БД список соперников

На текущий день он победил уже в 6 поединках.

Пожалуйста помогите Валентину вычеркнуть побеждённых соперников из списка, пока он сам на тренировке.
"""
import sqlite3
from typing import List

defeated_enemies = [
    "Иванов Э.",
    "Петров Г.",
    "Левченко Л.",
    "Михайлов М.",
    "Яковлев Я",
    "Кузнецов К.",
]


def remove_all_defeated_enemies(c: sqlite3.Cursor, defeated_enemies: List[str]) -> None:
    ...


if __name__ == "__main__":
    with sqlite3.connect("practise.db") as conn:
        cursor = conn.cursor()

        remove_all_defeated_enemies(cursor, defeated_enemies)
