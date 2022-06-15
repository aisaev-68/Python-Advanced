"""
Пожалуйста, запустите скрипт generate_practice_database.py прежде, чем приступать к выполнению практической работы. После выполнения скрипта у вас должен появиться файл базы practise.db
Параметризация запросов это очень важно (я не устану это повторять).
Давайте в качестве разминки напишем функцию,
    которая считывает список книг из файла построчно
    и добавляет их в БД practise.db в талицу table_books

При написании insert запроса, пожалуйста, используйте параметризованные SQL запросы.
"""
import sqlite3


def add_books_from_file(c: sqlite3.Cursor, file_name: str) -> None:
    ...


if __name__ == "__main__":
    with sqlite3.connect("practise.db") as conn:
        cursor = conn.cursor()

        add_books_from_file(cursor, "books_list.csv")
