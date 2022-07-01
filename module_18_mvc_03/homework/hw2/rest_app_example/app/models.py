import sqlite3
from dataclasses import dataclass
from typing import List, Optional, Union, Tuple

DATA = [
    {'id': 0, 'title': 'A Byte of Python', 'author': 'Swaroop C. H.'},
    {'id': 1, 'title': 'Moby-Dick; or, The Whale', 'author': 'Herman Melville'},
    {'id': 3, 'title': 'War and Peace', 'author': 'Leo Tolstoy'},
]

BOOKS_TABLE_AUTHOR = 'table_author'
BOOKS_TABLE_TITLE = 'table_title'


@dataclass
class Book:
    title: str
    author: str
    id_author: Optional[int] = None

    def __getitem__(self, item: str) -> Union[int, str]:
        return getattr(self, item)


def init_db(initial_records: List[dict]) -> None:
    with sqlite3.connect('table_books_hw2.db') as conn:
        cursor = conn.cursor()

        cursor.executescript(
            f'CREATE TABLE IF NOT EXISTS `{BOOKS_TABLE_AUTHOR}`'
            '(id_author INTEGER PRIMARY KEY AUTOINCREMENT, author)'
        )

        cursor.executescript(
            f'CREATE TABLE IF NOT EXISTS {BOOKS_TABLE_TITLE} '
            f'(id INTEGER PRIMARY KEY AUTOINCREMENT, title, '
            f'id_author INTEGER REFERENCES {BOOKS_TABLE_AUTHOR}(id_author))'
        )
        if not get_all_books():
            for item in initial_records:
                cursor.execute(
                    f'INSERT INTO `{BOOKS_TABLE_AUTHOR}` '
                    '(author) VALUES (?)',
                    (item['author'],)
                )

                id = cursor.lastrowid

                cursor.execute(
                    f'INSERT INTO `{BOOKS_TABLE_TITLE}` '
                    '(id_author, title) VALUES (?, ?)',
                    (id, item['title'])
                )


def _get_book_obj_from_row(row: Tuple) -> Book:
    return Book(id_author=row[0], author=row[1], title=row[2])


def get_all_books() -> List[Book]:
    with sqlite3.connect('table_books_hw2.db') as conn:
        cursor = conn.cursor()
        cursor.execute(f'SELECT db_author.id_author, '
                       f'db_author.author, db_title.title FROM `{BOOKS_TABLE_AUTHOR}` db_author '
                       f'JOIN {BOOKS_TABLE_TITLE} db_title ON db_title.id_author= db_author.id_author')
        all_books = cursor.fetchall()
        return [_get_book_obj_from_row(row) for row in all_books]


def add_author_and_book(book: Book) -> Book:
    with sqlite3.connect('table_books_hw2.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""INSERT INTO `{BOOKS_TABLE_AUTHOR}` (author) VALUES (?) """, (book.author,))

        book.id_author = cursor.lastrowid

        cursor.execute(
            f'INSERT INTO `{BOOKS_TABLE_TITLE}` '
            '(id_author, title) VALUES (?, ?)',
            (book.id_author, book.title)
        )
        return book


def get_book_by_id(book_id: int) -> Optional[Book]:
    with sqlite3.connect('table_books_hw2.db') as conn:
        cursor = conn.cursor()
        cursor.execute(f'SELECT db_author.id_author, '
                       f'db_author.author, db_title.title '
                       f'FROM {BOOKS_TABLE_AUTHOR} db_author '
                       f'JOIN {BOOKS_TABLE_TITLE} db_title ON db_title=db_author '
                       f'WHERE db_author.id_author = "%s"' % book_id)
        book = cursor.fetchone()
        if book:
            return _get_book_obj_from_row(book)


def update_book_by_id(book: Book) -> None:
    with sqlite3.connect('table_books_hw2.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            UPDATE {BOOKS_TABLE_AUTHOR} db_author
            SET db_author.author = ?
            WHERE id = ?
            """, (book.author, book.id_author)
        )

        cursor.execute(
            f"""
            UPDATE {BOOKS_TABLE_TITLE} db_title
            SET db_title.title = ? 
            WHERE id_author = ?
            """, (book.title, book.id_author)
        )
        conn.commit()


def delete_books_by_author(id_author) -> bool:
    with sqlite3.connect('table_books_hw2.db') as conn:
        cursor = conn.cursor()
        if get_author_by_id(id_author):
            cursor.execute(
                f"""
                DELETE FROM {BOOKS_TABLE_TITLE}
                WHERE id_author = ?
                """, (id_author,)
            )
            id = cursor.description
            cursor.execute(
                f"""
                DELETE FROM {BOOKS_TABLE_AUTHOR}
                WHERE id_author = ?
                """, (id_author,)
            )
            return True
        else:
            return False


def get_book_by_title(book_title: str) -> Optional[Book]:
    with sqlite3.connect('table_books_hw2.db') as conn:
        cursor = conn.cursor()

        cursor.execute(f'SELECT db_author.id_author, '
                       f'db_author.author, db_title.title '
                       f'FROM `{BOOKS_TABLE_AUTHOR}` db_author '
                       f'JOIN `{BOOKS_TABLE_TITLE}` db_title ON db_title.id_author = db_author.id_author '
                       f'WHERE db_title.title = "%s"' % book_title)
        book = cursor.fetchone()
        if book:
            return _get_book_obj_from_row(book)


def get_author(author: str) -> Optional[Book]:
    with sqlite3.connect('table_books_hw2.db') as conn:
        cursor = conn.cursor()

        cursor.execute(f'SELECT db_author.id_author, '
                       f'db_author.author, db_title.title '
                       f'FROM `{BOOKS_TABLE_AUTHOR}` db_author '
                       f'JOIN `{BOOKS_TABLE_TITLE}` db_title ON db_title.id_author = db_author.id_author '
                       f'WHERE db_author.author = "%s"' % author)
        book = cursor.fetchone()
        if book:
            return _get_book_obj_from_row(book)


def get_author_by_id(author_id: int) -> List[Book]:
    with sqlite3.connect('table_books_hw2.db') as conn:
        cursor = conn.cursor()
        cursor.execute(f'SELECT db_author.id_author, '
                       f'db_author.author, db_title.title '
                       f'FROM {BOOKS_TABLE_AUTHOR} db_author '
                       f'JOIN {BOOKS_TABLE_TITLE} db_title ON db_title.id_author=db_author.id_author '
                       f'WHERE db_author.id_author = "%s"' % author_id)
        all_books_for_author = cursor.fetchall()

        return [_get_book_obj_from_row(row) for row in all_books_for_author]


def add_book(book: Book) -> Book:
    with sqlite3.connect('table_books_hw2.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            f'INSERT INTO `{BOOKS_TABLE_TITLE}` '
            '(id_author, title) VALUES (?, ?)',
            (book.id_author, book.title)
        )
        return book
