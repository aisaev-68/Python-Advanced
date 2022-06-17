"""
Юный натуралист Петя решил посетить Юнтоловский заказник на рассвете и записать журнал всех птиц,
    которых он увидел в заказнике. Он написал программу, но, в процессе написания,
    так устал, что уснул на клавиатуре, отчего пол-программы стёрлось.

Наш юный натуралист точно помнит, что программа позволяла добавить в БД новую птицу и говорила ему,
    видел ли он такую птицу раньше.

Помогите восстановить исходный код программы ЮНат v0.1 ,
    реализовав функции log_bird (добавление новой птицы в БД) и check_if_such_bird_already_seen
    (проверка что мы уже видели такую птицу)

Пожалуйста помогите ему, реализовав функцию log_bird .
    При реализации не забудьте про параметризацию SQL запроса!
"""

import datetime
import sqlite3


def create_table(c: sqlite3.Cursor):
    sql_create_table = """
    CREATE TABLE IF NOT EXISTS `table_birds` 
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    date_time TEXT NOT NULL,
    bird_name TEXT NOT NULL)
    """
    c.execute(sql_create_table)

def log_bird(
        c: sqlite3.Cursor,
        bird_name: str,
        date_time: str,
) -> None:
    sql_add_bird = """
    INSERT INTO `table_birds` (date_time, bird_name)
    VALUES(?, ?)
    """
    c.execute(sql_add_bird, (date_time, bird_name))


def check_if_such_bird_already_seen(c: sqlite3.Cursor, bird_name: str) -> bool:
    sql_select_bird = """
    SELECT COUNT(*)  
    FROM `table_birds`  
    WHERE  bird_name = ? 
    """
    c.execute(sql_select_bird, (bird_name,))
    count = c.fetchone()[0]
    if count:
        return True
    else:
        return False


if __name__ == "__main__":
    print("Программа помощи ЮНатам v0.1")
    count_str = input("Сколько птиц вы увидели?\n> ")
    count = int(count_str)

    with sqlite3.connect("hw.db") as connection:
        cursor = connection.cursor()
        create_table(cursor)
        for _ in range(count):
            right_now = datetime.datetime.utcnow().isoformat()
            name = input("Пожалуйста введите имя птицы\n> ")
            if check_if_such_bird_already_seen(cursor, name):
                print("Такую птицу мы уже наблюдали!")
            else:
                print("Такую птицу мы еще не наблюдали!")
                log_bird(cursor, name, right_now)
