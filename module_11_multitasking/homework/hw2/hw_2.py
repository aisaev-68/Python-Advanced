import json
import logging
import sqlite3
import time

import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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
        cursor.execute("""CREATE TABLE IF NOT EXISTS peoples (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        birth_year TEXT,
        gender TEXT 
        )""")
        if select(value):
            cursor.execute("""INSERT INTO peoples (name, birth_year, gender) VALUES (?, ?, ?)""", value)


def query(numb: int) -> None:
    url = f'https://swapi.dev/api/people/{numb}/'
    response = requests.get(url, timeout=5)

    if response.status_code == 200:
        data = json.loads(response.content)
        if data.get('name') and data.get('birth_year') and data.get('gender'):
            insert((data['name'], data['birth_year'], data['gender']))


if __name__ == "__main__":
    start = time.time()
    for i in range(1, 22):
        query(i)
    logger.info('Done in {:.4}'.format(time.time() - start))
