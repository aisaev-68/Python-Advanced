import datetime
from typing import Any
from sqlalchemy import exists, func, cast, VARCHAR, desc
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.dialects.sqlite import DATETIME

from database import Session, session, Authors, Books, Students, ReceivingBook
from create_database import _load_fake_data


def check_table_exists(session: Session, id: int) -> bool:
    is_exists = session.query(exists().where(Authors.id == id)).scalar()

    return is_exists


def insert_data(load_fake_data: bool = True):
    if not check_table_exists(session, 1):
        if load_fake_data:
            _load_fake_data(session)


def get_author_by_id(id_author: int) -> list:
    return session.query(Authors).filter(Authors.id == id_author).one_or_none()


def get_count_books_for_author(id_author: int):
    books_list = []
    join_books = session.query(Authors.id, Authors.first_name, Authors.last_name, Books.name,
                               Books.count).join(Books)
    books_for_author = join_books.filter(Authors.id == id_author).all()
    # [(1, 'Дорофеев', 'Святополк', 'Ускорение действенных пользователей', 13)]
    for book in books_for_author:
        books_as_dict = {'id': book[0], 'firstname': book[1],
                         'lastname': book[2], 'title': book[3],
                         'amount': book[4]}
        books_list.append(books_as_dict)
    return books_list


def get_search_books(txt: str) -> list:
    text = '%' + txt + "%"
    return session.query(Books).filter(Books.name.ilike(text)).all()


def get_all_books() -> list:
    return session.query(Books).all()


def get_books() -> list:
    book_list = []
    books = session.query(Books).filter(Books.count > 0).all()
    for book in books:
        book_as_dict = book.to_json()
        book_list.append(book_as_dict)
    return book_list


def get_book_by_id(id_book: int, flag_count: bool) -> '__main__.Book':
    if flag_count:
        return session.query(Books).filter(Books.id == id_book, Books.count > 0).one_or_none()
    else:
        return session.query(Books).filter(Books.id == id_book).one_or_none()


def update_count_book_by_id(id_book: int, count: int) -> Any:
    try:
        session.query(Books).filter(Books.id == id_book).update({"count": count},
                                                                synchronize_session="fetch")
        session.commit()
    except SQLAlchemyError:
        session.rollback()
        return {'error': 'error'}
    return True


def get_all_students() -> list:
    return session.query(Students).all()


def get_list_students() -> list:
    return session.query(Students).filter(Students.scholarship == True).all()


def get_list_students_avgscope(mark: float) -> list:
    return session.query(Students).filter(Students.average_score > mark).all()


def get_student_by_id(id_student: int) -> list:
    return session.query(Students).filter(Students.id == id_student).one_or_none()


def add_issue_book(*args) -> None:
    date_issue = datetime.datetime.today()
    update_count_book_by_id(args[0], args[2])
    session.add(ReceivingBook(book_id=args[0], student_id=args[1], date_of_issue=date_issue))
    session.commit()


def update_return_date(*args) -> Any:
    try:
        update_count_book_by_id(args[0], args[2])
        session.query(ReceivingBook).filter(ReceivingBook.book_id ==
                                            args[0], ReceivingBook.student_id ==
                                            args[1]).update({"date_of_return": datetime.datetime.today()},
                                                            synchronize_session="fetch")
        session.commit()
    except SQLAlchemyError:
        session.rollback()
        return {'error': 'error'}
    return True


def get_issue_book(id_book: int, id_student: int) -> list:
    return session.query(ReceivingBook).filter(ReceivingBook.book_id == id_book,
                                               ReceivingBook.student_id == id_student).all()


def get_count_date_with_book() -> list:
    debtors_list = []
    debtors_student = session.query(ReceivingBook).filter(ReceivingBook.count_date_with_book > 14,
                                                          ReceivingBook.date_of_return == None).all()
    for student in debtors_student:
        debtors_as_dict = student.to_json()
        debtors_list.append(debtors_as_dict)
    return debtors_list


def get_havents_read(id_student: int, id_author: int):
    hevent_list = []
    books_read_by_student = session.query(Students.id).join(ReceivingBook).filter(Students.id == id_student)
    hevent_books = session.query(Authors.id, Authors.first_name, Authors.last_name, Books.id, Books.name).join(
        Books).filter(Books.id != books_read_by_student, Authors.id == id_author).all()
    for raw in hevent_books:
        hevent_as_dict = {'author_id': raw[0], 'first_name': raw[1], 'last_name': raw[2], 'books_id': raw[3],
                          'title': raw[4]}
        hevent_list.append(hevent_as_dict)
    return hevent_list


def get_avg_count_books_by_month():
    date_today = str(datetime.datetime.today())[:7] + "%"
    all_books_read = session.query(ReceivingBook.student_id, func.count(ReceivingBook.student_id).label('books_count')). \
        filter(cast(ReceivingBook.date_of_issue, VARCHAR(23)).like(date_today)).group_by(
        ReceivingBook.student_id).subquery()
    avg_books = session.query(func.avg(all_books_read.c.books_count)).one_or_none()
    return avg_books[0]


def popular_book():
    popular_book = session.query(ReceivingBook.book_id, func.count().label('count')
                                 ).join(Students).filter(
        Students.average_score > 4.0
    ).group_by(ReceivingBook.book_id).order_by(desc('count')).limit(1).one_or_none()
    id_book = popular_book[0]
    author_book = session.query(Books.id, Authors.first_name, Authors.last_name,
                                Books.name).join(Books).filter(Books.id == id_book).one_or_none()
    return {'id_book': author_book[0],
            'author_firstname': author_book[1],
            'author_lastname': author_book[2],
            'title': author_book[3]
            }


def most_reading_students():
    most_list = []
    sql_most_read = session.query(Students.surname, Students.name, func.count().label('count')
                                  ).join(ReceivingBook).group_by(Students.surname, Students.name
                                                                 ).order_by(desc('count')).limit(10).all()
    for row in sql_most_read:
        most_as_dict = {'first_name': row[0],
                        'last_name': row[1],
                        'amount_books': row[2]}
        most_list.append(most_as_dict)
    return most_list


def insert_many_students(lst: list):
    session.bulk_insert_mappings(Students, lst, )
    session.commit()
