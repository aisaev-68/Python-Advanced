"""
Для каждого поля и валидатора в endpoint /registration напишите по unit-тесту,
    который проверит, что валидатор и правда работает (т.е. мы должны проверить,
    что существует набор данных, которые проходят валидацию, и такие,
    которые валидацию не проходят)
"""

import unittest

from hw_1_2 import app


class TestDecrypt(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config["WTF_CSRF_ENABLED"] = False
        self.registration = app.test_client()

    def test_registration(self):
        data = {'email': 'user@user.ru', 'phone': 9992344545,
                'name': 'Tom', 'address': 'Moscow', 'index': '234',
                'comment': 'Hello, world'}
        response = self.registration.post('/registration', data=data)
        response_text = response.data.decode()
        print(response_text)
        self.assertTrue(response.status_code == 200)


if __name__ == '__main__':
    unittest.main()
