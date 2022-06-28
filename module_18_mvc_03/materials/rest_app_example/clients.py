import json
import typing as tp

import requests

import logging
logging.basicConfig(level=logging.DEBUG)


class BookClient:

    URL = 'http://0.0.0.0:5000/api/books'
    TIMEOUT = 5

    def __init__(self):
        self._session = requests.Session()

    def get_all_books(self) -> tp.Dict:
        response = self._session.get(self.URL, timeout=self.TIMEOUT)
        return response.json()

    def add_new_book(self, data: tp.Dict):
        response = self._session.post(self.URL, json=data, timeout=self.TIMEOUT)
        if response.status_code == 201:
            return response.json()
        else:
            raise ValueError('Wrong params. Response message: {}'.format(response.json()))


if __name__ == '__main__':
    c = BookClient()
    c._session.post(c.URL, data=json.dumps({'title': '123', 'author': 'name'}), headers={'content-type': 'application/json'})

