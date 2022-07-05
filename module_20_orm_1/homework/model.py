import datetime
from pprint import pprint
from typing import Dict, Any

from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, Float, Boolean, func
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.hybrid import hybrid_property

engine = create_engine("sqlite:///library.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)

    def __repr__(self):
        return f"{self.first_name}, {self.last_name}"

    @classmethod
    def get_author_by_id(cls, id_author: int) -> list:
        return session.query(Author).filter(Author.id == id_author).one_or_none()


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    count = Column(Integer, nullable=False, default=1)
    release_date = Column(DateTime, nullable=False)
    author_id = Column(Integer, nullable=False)

    @classmethod
    def get_search_books(cls, txt: str) -> list:
        text = '%' + txt + "%"
        return session.query(Book).filter(Book.name.ilike(text)).all()

    @classmethod
    def get_all_books(cls) -> list:
        return session.query(Book).all()

    @classmethod
    def get_books(cls) -> list:
        return session.query(Book).filter(Book.count > 0).all()

    @classmethod
    def get_book_by_id(cls, id_book: int, flag_count: bool) -> '__main__.Book':
        if flag_count:
            return session.query(Book).filter(Book.id == id_book, Book.count > 0).one_or_none()
        else:
            return session.query(Book).filter(Book.id == id_book).one_or_none()

    @classmethod
    def update_count_book_by_id(cls, id_book: int, count: int) -> Any:
        try:
            session.query(Book).filter(Book.id == id_book).update({"count": count}, synchronize_session="fetch")
            session.commit()
        except SQLAlchemyError:
            cls.session.rollback()
            return {'error': 'error'}
        return True

    def to_json(self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    surname = Column(String(100), nullable=False)
    phone = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    average_score = Column(Float, nullable=False)
    scholarship = Column(Boolean, nullable=False)

    @classmethod
    def get_all_students(cls) -> list:
        return session.query(Student).all()

    @classmethod
    def get_list_students(cls) -> list:
        return session.query(Student).filter(Student.scholarship == True).all()

    @classmethod
    def get_list_students_avgscope(cls, mark: float) -> list:
        return session.query(Student).filter(Student.average_score > mark).all()

    def to_json(self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @classmethod
    def get_student_by_id(cls, id_student: int) -> list:
        return session.query(Student).filter(Student.id == id_student).one_or_none()


class ReceivingBook(Base):
    __tablename__ = 'receiving_books'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, nullable=False)
    student_id = Column(Integer, nullable=False)
    date_of_issue = Column(DateTime, nullable=False)
    date_of_return = Column(DateTime)

    @hybrid_property
    def count_date_with_book(self) -> int:
        now = datetime.datetime.now()
        diff = now - self.date_of_issue
        return diff.days

    @count_date_with_book.expression
    def count_date_with_book(cls) -> int:
        strftime = func.strftime
        diff = strftime('%Y%m%d', 'now') - strftime('%Y%m%d', cls.date_of_issue)
        return diff

    @classmethod
    def get_count_date_with_book(cls) -> list:
        sql = session.query(ReceivingBook).filter(ReceivingBook.count_date_with_book > 14,
                                                  ReceivingBook.date_of_return == None).all()
        return sql

    @classmethod
    def add_issue_book(cls, *args) -> None:
        date_issue = datetime.datetime.today() + datetime.timedelta(days=30)
        Book.update_count_book_by_id(args[0], args[2])
        session.add(ReceivingBook(book_id=args[0], student_id=args[1], date_of_issue=date_issue))

        session.commit()

    @classmethod
    def update_return_date(cls, *args) -> Any:
        try:
            Book.update_count_book_by_id(args[0], args[2])
            session.query(ReceivingBook).filter(ReceivingBook.book_id == args[0],
                                                ReceivingBook.student_id == args[1]).update(
                {"date_of_return": datetime.datetime.today()}, synchronize_session="fetch")

            session.commit()
        except SQLAlchemyError:
            cls.session.rollback()
            return {'error': 'error'}
        return True

    @classmethod
    def get_issue_book(cls, id_book: int, id_student: int) -> list:
        return session.query(ReceivingBook).filter(ReceivingBook.book_id == id_book,
                                                   ReceivingBook.student_id == id_student).all()

    def to_json(self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
