import datetime
import random

from faker import Faker
from model import Author, Book, Student, ReceivingBook, session, Base, engine

fake = Faker('ru_RU')

def generate_authors(numb: int) -> tuple:
    """Return ('first_name', 'last_name', 'gender')"""
    set_act = set()
    while True:
        g = 'М' if random.randint(0, 1) == 0 else 'Ж'
        first_name = fake.first_name_male() if g == 'М' else fake.first_name_female()
        last_name = fake.last_name_male() if g == 'М' else fake.last_name_female()
        set_act.add((last_name, first_name, g))
        if len(set_act) == numb:
            break

    return tuple(set_act)


def generate_students(numb: int) -> tuple:
    """numb - количество студентов,
    Return ('first_name', 'last_name')"""
    set_dir = set()
    while True:
        g = 'М' if random.randint(0, 1) == 0 else 'Ж'
        first_name = fake.first_name_male() if g == 'М' else fake.first_name_female()
        last_name = fake.last_name_male() if g == 'М' else fake.last_name_female()
        set_dir.add((last_name, first_name))
        if len(set_dir) == numb:
            break
    return tuple(set_dir)


def generate_books() -> str:
    return fake.bs()


def generate_date():
    return fake.date_time()


def generate_phone():
    return fake.phone_number()


def generate_email():
    return fake.email()


def insert_data():
    Base.metadata.create_all(engine)
    i = 0
    for row in generate_authors(10):
        i += 1
        session.add(Author(first_name=row[0], last_name=row[1]))
        session.add(Book(name=generate_books(), count=random.randint(1, 15),
                         release_date=generate_date(), author_id=i))
        session.commit()

    for row in generate_students(30):
        session.add(Student(surname=row[0], name=row[1], phone=generate_phone(), email=generate_email(),
                            average_score=random.uniform(0.0, 10.0), scholarship=random.choice([False, True])))

        session.commit()
    a = datetime.datetime.today() + datetime.timedelta(days=30)
    session.add(ReceivingBook(book_id=1, student_id=1, date_of_issue=a))
    session.add(ReceivingBook(book_id=2, student_id=2, date_of_issue=a))
    a = datetime.datetime.today() - datetime.timedelta(days=30)
    session.add(ReceivingBook(book_id=4, student_id=3, date_of_issue=a))
    session.add(ReceivingBook(book_id=5, student_id=4, date_of_issue=a))
    session.add(ReceivingBook(book_id=3, student_id=5, date_of_issue=a))
    session.commit()
