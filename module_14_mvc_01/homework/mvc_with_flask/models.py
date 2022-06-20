import sqlite3
from typing import List


DATA = [
    {'id': 0, 'title': 'A Byte of Python', 'author': 'Swaroop C. H.'},
    {'id': 1, 'title': 'Moby-Dick; or, The Whale', 'author': 'Herman Melville'},
    {'id': 3, 'title': 'War and Peace', 'author': 'Leo Tolstoy'},
]


class Book:

    def __init__(self, id: int, title: str, author: str):
        self.id = id
        self.title = title
        self.author = author


    def __getitem__(self, item):
        return getattr(self, item)


def init_db(initial_records: List[dict]):
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()

        cursor.executescript(
            'CREATE TABLE IF NOT EXISTS `table_books`'
            '(id INTEGER PRIMARY KEY AUTOINCREMENT, title, author)'
        )
        cursor.executescript(
            'CREATE TABLE IF NOT EXISTS `table_counter`'
            '(id INTEGER PRIMARY KEY AUTOINCREMENT, id_count INTEGER, counter INTEGER'
            'FOREIGN KEY id_count REFERENCES `table_books` (id))'
        )
        cursor.executemany(
            'INSERT INTO `table_books` '
            '(title, author) VALUES (?, ?)',
            [(item['title'], item['author']) for item in initial_records]
        )


def get_all_books() -> List[Book]:
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * from `table_books`')
        all_books = cursor.fetchall()
        return [Book(*row) for row in all_books]


def add_book(value):
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO `table_books` '
            '(title, author) VALUES (?, ?)',
            value
        )


def search_book(value) -> List[Book]:
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT * FROM `table_books` '
            'WHERE author = ?', (value,)

        )
        data = cursor.fetchall()
        return [Book(*row) for row in data]


def update_book_counter(value):
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            'UPDATE `table_counter`  SET counter = ?'
            'WHERE id_count = ?', value
        )


def insert_book_counter(value):
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO `table_counter`'
            '(id_count, counter) VALUES (?, ?)', value
        )


def select_book_counter(value):
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT * FROM `table_counter`'
            'WHERE id_count = ?', value
        )

        data = cursor.fetchall()
        return data