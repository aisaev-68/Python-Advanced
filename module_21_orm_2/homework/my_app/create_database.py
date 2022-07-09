import csv
import datetime
import random

from faker import Faker

from database import Session, Authors, Books, Students, ReceivingBook

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


def generate_students(numb: int) -> list:
    """numb - количество студентов,
    Return ('first_name', 'last_name')"""
    students_list = []
    while True:
        g = 'М' if random.randint(0, 1) == 0 else 'Ж'
        first_name = fake.first_name_male() if g == 'М' else fake.first_name_female()
        last_name = fake.last_name_male() if g == 'М' else fake.last_name_female()

        student_as_dict = {
            'name': last_name,
            'surname': first_name,
            'phone': generate_phone(),
            'email': generate_email(),
            'average_score': random.uniform(0.0, 10.0),
            'scholarship': random.choice([False, True])
        }
        students_list.append(student_as_dict)
        if len(students_list) == numb:
            break
    return students_list


def generate_books() -> str:
    return fake.bs()


def generate_date():
    return fake.date_time()


def generate_phone():
    return fake.phone_number()


def generate_email():
    return fake.email()


def _load_fake_data(session: Session):
    for id, raw in enumerate(generate_authors(10)):
        session.add(Authors(first_name=raw[0], last_name=raw[1]))

        for _ in range(random.randint(1, 10)):
            session.add(Books(name=generate_books(), count=random.randint(1, 15),
                              release_date=generate_date(), author_id=id + 1))

    session.commit()

    session.bulk_insert_mappings(Students, generate_students(50), )
    session.commit()

    a = datetime.datetime.today()
    # + datetime.timedelta(days=30)
    b = datetime.datetime.today() - datetime.timedelta(days=30)
    session.add(ReceivingBook(book_id=1, student_id=1, date_of_issue=a))
    session.add(ReceivingBook(book_id=2, student_id=2, date_of_issue=a))
    session.add(ReceivingBook(book_id=3, student_id=3, date_of_issue=b))
    session.add(ReceivingBook(book_id=4, student_id=4, date_of_issue=a))
    session.add(ReceivingBook(book_id=5, student_id=5, date_of_issue=b))

    session.commit()
    session.bulk_insert_mappings(Students, generate_students(5), )
    session.commit()

    # with open('download/students.csv', 'w', encoding='utf=8') as file:
    #     for raw in generate_students(50):
    #         line = raw[0] + ';' + raw[1] + ';' + generate_phone() + ';' + generate_email() + ';' +\
    #         str(random.uniform(0.0, 10.0)) + ';' + str(random.choice([False, True])) +'\n'
    #         file.writelines(line)

    with open('download/students.csv', 'w', encoding='utf=8') as f:
        writer = csv.DictWriter(
            f, delimiter=';', fieldnames=list(generate_students(1)[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for d in generate_students(50):
            writer.writerow(d)
