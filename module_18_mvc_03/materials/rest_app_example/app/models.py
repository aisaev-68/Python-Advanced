import sqlite3
from dataclasses import dataclass
from typing import List, Optional, Union, Tuple

DATA = [
    {'id': 0, 'title': 'A Byte of Python', 'author': 'Swaroop C. H.'},
    {'id': 1, 'title': 'Moby-Dick; or, The Whale', 'author': 'Herman Melville'},
    {'id': 3, 'title': 'War and Peace', 'author': 'Leo Tolstoy'},
]

BOOKS_TABLE_NAME = 'books'


@dataclass
class Book:
    title: str
    author: str
    id: Optional[int] = None

    def __getitem__(self, item: str) -> Union[int, str]:
        return getattr(self, item)


def init_db(initial_records: List[dict]) -> None:
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT name FROM sqlite_master "
            f"WHERE type='table' AND name='{BOOKS_TABLE_NAME}';"
        )
        exists = cursor.fetchone()
        # now in `exist` we have tuple with table name if table really exists in DB
        if not exists:
            cursor.executescript(
                f'CREATE TABLE `{BOOKS_TABLE_NAME}`'
                '(id INTEGER PRIMARY KEY AUTOINCREMENT, title, author)'
            )
            cursor.executemany(
                f'INSERT INTO `{BOOKS_TABLE_NAME}` '
                '(title, author) VALUES (?, ?)',
                [(item['title'], item['author']) for item in initial_records]
            )


def _get_book_obj_from_row(row: Tuple) -> Book:
    return Book(id=row[0], title=row[1], author=row[2])


def get_all_books() -> List[Book]:
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM `{BOOKS_TABLE_NAME}`')
        all_books = cursor.fetchall()
        return [_get_book_obj_from_row(row) for row in all_books]


def add_book(book: Book) -> Book:
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            INSERT INTO `{BOOKS_TABLE_NAME}` 
            (title, author) VALUES (?, ?)
            """,
            (book.title, book.author)
        )
        book.id = cursor.lastrowid
        return book


def get_book_by_id(book_id: int) -> Optional[Book]:
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM `{BOOKS_TABLE_NAME}` WHERE id = "%s"' % book_id)
        book = cursor.fetchone()
        if book:
            return _get_book_obj_from_row(book)


def update_book_by_id(book: Book) -> None:
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            UPDATE {BOOKS_TABLE_NAME}
            SET title = ? ,
                author = ?
            WHERE id = ?
            """, (book.title, book.author, book.id)
        )
        conn.commit()


def delete_book_by_id(book_id: int) -> None:
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            DELETE {BOOKS_TABLE_NAME}
            WHERE id = ?
            """, (book_id,)
        )
        conn.commit()


def get_book_by_title(book_title: str) -> Optional[Book]:
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            f'SELECT * FROM `{BOOKS_TABLE_NAME}` WHERE title = "%s"' % book_title
        )
        book = cursor.fetchone()
        if book:
            return _get_book_obj_from_row(book)
