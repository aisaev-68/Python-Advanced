import json
import logging
import sqlite3
import time
import requests
import multiprocessing


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_db():
    with sqlite3.connect("swap.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS peoples (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        birth_year TEXT,
        gender TEXT 
        )""")
        logger.info('База данных swap.db с таблицей peoples создана')


def select(data: tuple) -> bool:
    with sqlite3.connect("swap.db") as conn:
        cursor = conn.cursor()
        sql = "SELECT * FROM peoples WHERE name=? AND birth_year=? AND gender=?"
        cursor.execute(sql, data)
        result = cursor.fetchall()

    if result:
        return False
    else:
        return True


def insert(value: tuple) -> None:
    with sqlite3.connect("swap.db") as conn:
        cursor = conn.cursor()
        if select(value):
            cursor.execute("INSERT INTO peoples (name, birth_year, gender) VALUES (?, ?, ?)", value)
            logger.info(f'Данные {value} загружены в базу')
        else:
            logger.info(f'Данные {value} уже есть в базе')


def query(numb: int) -> None:
    url = f'https://swapi.dev/api/people/{numb}/'

    logger.info(f'С сайта запрошены данне на {numb} человека')
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
        data = json.loads(response.content)
        if data.get('name') and data.get('birth_year') and data.get('gender'):
            value = (data['name'], data['birth_year'], data['gender'])
            logger.info(f'Данные {value} отправлены для загрузки в базу')
            insert(value)
    else:
        logger.info(f'Сервер вернул ответ {response.status_code}')


def main_multiprocessing() -> None:
    start = time.time()
    with multiprocessing.Pool(processes=22) as pool:
        pool.map(query, range(1, 23))

    logger.info('Done in {:.4}'.format(time.time() - start))


if __name__ == "__main__":
    create_db()
    main_multiprocessing()


