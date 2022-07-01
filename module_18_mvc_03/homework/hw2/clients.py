import json
import random
import typing as tp
import aspose
import requests
from faker import Faker

import logging

logging.basicConfig(filename='sessions.log', filemode='w', level=logging.DEBUG,
                    format='| %(asctime)s | %(filename)s:%(lineno)d | %(levelname)s | %(message)s |',
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

fake = Faker('ru_RU')


def generate_author() -> str:
    """Return 'first_name last_name')"""

    g = 'М' if random.randint(0, 1) == 0 else 'Ж'
    first_name = fake.first_name_male() if g == 'М' else fake.first_name_female()
    last_name = fake.last_name_male() if g == 'М' else fake.last_name_female()

    return f'{last_name} {first_name}'


def generate_title() -> str:
    """Return 'title'"""

    return fake.bs()


class AuthorClient:
    URL = 'http://127.0.0.1:5000/api/authors'
    TIMEOUT = 5

    def __init__(self):
        self._session = requests.Session()

    def get_all_author(self) -> tp.Dict:
        response = self._session.get(self.URL, timeout=self.TIMEOUT)
        return response.json()

    def add_new_author(self, data: tp.Dict):
        response = self._session.post(self.URL, json=data, timeout=self.TIMEOUT)
        if response.status_code == 201:
            return response.json()
        else:
            raise ValueError('Wrong params. Response message: {}'.format(response.json()))

    def delete_author_and_book(self):
        response = self._session.delete(self.URL, timeout=self.TIMEOUT)
        if response.status_code == 201:
            return response.json()
        else:
            raise ValueError('Wrong params. Response message: {}'.format(response.json()))


def main_sessios(numb: int, ses: str):
    logger.info(f'Sending {numb} data insert requests (Modul {ses})')
    for i in range(numb):
        c._session.post(c.URL, data=json.dumps({'title': generate_title(), 'author': generate_author()}),
                        headers={'content-type': 'application/json'})
    logger.info(f'{numb} records inserted into the database (Modul {ses})')


def main_requests(numb: int, ses: str):
    logger.info(f'Sending {numb} data insert requests (Modul {ses})')
    for i in range(numb):
        requests.post(c.URL, data=json.dumps({'title': generate_title(), 'author': generate_author()}),
                      headers={'content-type': 'application/json'})
    logger.info(f'{numb} records inserted into the database (Modul {ses})')


if __name__ == '__main__':
    c = AuthorClient()
    main_sessios(10, 'session')
    main_sessios(50, 'session')
    main_sessios(100, 'session')

    main_requests(10, 'requests')
    main_requests(50, 'requests')
    main_requests(100, 'requests')
