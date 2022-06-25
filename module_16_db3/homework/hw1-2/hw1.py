import random
import sqlite3
from pprint import pprint

from faker import Faker

fake = Faker('ru_RU')


def init_db() -> None:
    with sqlite3.connect('films.db') as conn:
        cursor = conn.cursor()

        cursor.executescript(
            'CREATE TABLE IF NOT EXISTS director '
            '(dir_id INTEGER PRIMARY KEY, dir_first_name VARCHAR(50), '
            'dir_last_name VARCHAR(50));'


            'CREATE TABLE IF NOT EXISTS `movie` '
            '(mov_id INTEGER PRIMARY KEY, mov_title VARCHAR(50));'


            'CREATE TABLE IF NOT EXISTS `actors` '
            '(act_id INTEGER PRIMARY KEY, act_first_name VARCHAR(50), '
            'act_last_name VARCHAR(50), act_gender VARCHAR(1));'


            'CREATE TABLE IF NOT EXISTS `movie_direction` '
            '(dir_id INTEGER REFERENCES director(dir_id), '
            'mov_id INTEGER REFERENCES movie(mov_id));'


            'CREATE TABLE IF NOT EXISTS `oscar_awarded` '
            '(award_id INTEGER PRIMARY KEY, '
            'mov_id INTEGER REFERENCES movie(mov_id));'


            'CREATE TABLE IF NOT EXISTS `movie_cast` '
            '(act_id INTEGER REFERENCES actors(act_id), '
            'mov_id INTEGER REFERENCES movie(mov_id), '
            'role VARCHAR(50))'
        )


def generate_actors(numb: int) -> tuple:
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


def generate_directors(numb: int) -> tuple:
    """numb - количество режиссеров,
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


def generate_title(numb: int) -> tuple:
    """Return ('mov_title')"""
    set_title = set()
    while True:
        set_title.add((fake.bs(),))
        if len(set_title) == numb:
            break
    return tuple(set_title)


def generate_role(numb: int) -> tuple:
    """Return ('role',)"""
    set_rol = set()
    while True:
        set_rol.add((fake.word(),))
        if len(set_rol) == numb:
            break

    return tuple(set_rol)


def get_max_id_directors() -> list:
    with sqlite3.connect('films.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            'select max(dir_id) from director')

        return cursor.fetchall()


def select_directors() -> list:
    with sqlite3.connect('films.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            'select * from director')

        return cursor.fetchall()


def select_movie() -> list:
    with sqlite3.connect('films.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            'select * from movie')

        return cursor.fetchall()


def get_max_id_movie() -> list:
    with sqlite3.connect('films.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            'select max(mov_id) from movie')

        return cursor.fetchall()


def select_actors() -> list:
    with sqlite3.connect('films.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            'select * from actors')

        return cursor.fetchall()


def get_max_id_actors() -> list:
    with sqlite3.connect('films.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            'select max(act_id) from actors')

        return cursor.fetchall()


def get_max_id_oscar() -> list:
    with sqlite3.connect('films.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            'select max(award_id) from oscar_awarded')

        return cursor.fetchall()


def directors_number_of_films() -> list:
    """
    Количество фильмов каждого режиссера
    :return: list
    """
    with sqlite3.connect('films.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            'select director.dir_first_name, director.dir_last_name, count(*) from director '
            'join movie_direction md on director.dir_id = md.dir_id '
            'join movie m on m.mov_id = md.mov_id '
            'group by director.dir_first_name')

        return cursor.fetchall()


def insert_data():
    with sqlite3.connect('films.db') as conn:
        cursor = conn.cursor()
        for id, director in enumerate(generate_directors(20)):
            cursor.execute(
                'insert into director(dir_id, dir_first_name, dir_last_name) '
                'values (?, ?, ?)', (id + 1, director[0], director[1]))

        for id, mov_title in enumerate(generate_title(1000)):
            cursor.execute(
                'insert into movie(mov_id, mov_title) '
                'values (?, ?)', (id + 1, mov_title[0]))


    with sqlite3.connect('films.db') as conn:
        cursor = conn.cursor()
        # 20 directors
        id_dir = [row[0] for row in select_directors()]

        # 1000 movie
        id_mov = [row[0] for row in select_movie()]
        id_act = 0
        mov_cast = generate_role(200)
        for ind, id_m in enumerate(id_mov):
            id_d = random.choice(id_dir)
            cursor.execute(
                'insert into movie_direction(dir_id, mov_id) '
                'values (?, ?)', (id_d, id_m))


            m_cast = random.choice(mov_cast)
            actor = generate_actors(10)
            for raw in actor:
                id_act += 1
                cursor.execute(
                    'insert into actors(act_id, act_first_name, act_last_name, act_gender) '
                    'values (?, ?, ?, ?)', (id_act, raw[0], raw[1], raw[2]))

                cursor.execute(
                    'insert into movie_cast(act_id, mov_id, role) '
                    'values (?, ?, ?)', (id_act, id_m, m_cast[0]))




    for index, id in enumerate(id_mov[:100]):
            cursor.execute(
                'insert into oscar_awarded(award_id, mov_id) '
                'values (?, ?)', (index + 1, id))


if __name__ == '__main__':
    init_db()
    if not select_directors():
        print('Заполняю базу...')
        insert_data()
        print('База заполнена')
    else:
        print('База готова к работе\n')

    pprint([{'first_name': row[0], 'last_name': row[1],
             'count_movie': row[2]} for row in directors_number_of_films()])

