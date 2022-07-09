import datetime
import re

from sqlalchemy import create_engine, Integer, String, \
    Column, DateTime, ForeignKey, Float, Boolean, func, event
from sqlalchemy.orm import sessionmaker, backref, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property

DATABASE_NAME = 'library.db'
tables = ['authors', 'books', 'students', 'receiving_books']

engine = create_engine(f"sqlite:///{DATABASE_NAME}", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


def create_db():
    Base.metadata.create_all(engine)


def drop_table():
    for table_name in tables:
        table = Base.metadata.tables.get(table_name)
        if table is not None:
            Base.metadata.drop_all(bind=engine, tables=[table], checkfirst=True)


class Authors(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    author = relationship("Books", back_populates="book", lazy='joined', cascade="all, delete-orphan")

    def to_json(self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Books(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    count = Column(Integer, nullable=False, default=1)
    release_date = Column(DateTime, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id', ondelete='CASCADE'))
    book = relationship("Authors", back_populates="author")
    rec_books = association_proxy('receiving_book', 'rec_books')

    def to_json(self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Students(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    surname = Column(String(100), nullable=False)
    phone = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    average_score = Column(Float, nullable=False)
    scholarship = Column(Boolean, nullable=False)
    rec_students = association_proxy('receiving_book', 'rec_students')

    def to_json(self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class ReceivingBook(Base):
    __tablename__ = 'receiving_books'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    student_id = Column(Integer, ForeignKey('students.id'))
    date_of_issue = Column(DateTime, nullable=False)
    date_of_return = Column(DateTime)
    rec_students = relationship(Students, backref=backref("receiving_book"), lazy='selectin')
    rec_books = relationship(Books, backref=backref("receiving_book"))

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

    def to_json(self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


@event.listens_for(Students, 'before_insert')
def validate_phone(target, *args, **kwargs):
    phone = kwargs.get('phone')
    if phone and re.search(r'\+7\(9\d{2}\)\-\d{3}\-\d{2}\-\d{2}', phone):
        raise ValueError('Неправильный номер телефона')

