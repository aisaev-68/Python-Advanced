"""
Для каждого поля и валидатора в endpoint /registration напишите по unit-тесту,
    который проверит, что валидатор и правда работает (т.е. мы должны проверить,
    что существует набор данных, которые проходят валидацию, и такие,
    которые валидацию не проходят)
"""

import unittest

from hw_1_2 import app

data = {'email': 'user@user.ru', 'phone': '9992344545',
        'name': 'Tom', 'address': 'Moscow', 'index': '234',
        'comment': 'Hello, world'}


class TestDecrypt(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config["WTF_CSRF_ENABLED"] = False
        self.registration = app.test_client()

    def test_registration(self):
        response = self.registration.post('/registration', data=data)
        self.assertTrue(response.status_code == 200)

    def test_email1(self):
        data['email'] = 'useruser.ru'
        response = self.registration.post('/registration', data=data)
        self.assertEqual(response.status_code, 200)

    def test_email2(self):
        data['email'] = 'user@userru'
        response = self.registration.post('/registration', data=data)
        self.assertEqual(response.status_code, 200)

    def test_email3(self):
        data['email'] = ''
        response = self.registration.post('/registration', data=data)
        self.assertEqual(response.status_code, 200)

    def test_phone1(self):
        data['phone'] = '12345678912'
        response = self.registration.post('/registration', data=data)
        self.assertEqual(response.status_code, 200)

    def test_phone2(self):
        data['phone'] = '12345'
        response = self.registration.post('/registration', data=data)
        self.assertEqual(response.status_code, 200)

    def test_phone3(self):
        data['phone'] = ''
        response = self.registration.post('/registration', data=data)
        self.assertEqual(response.status_code, 200)

    def test_name(self):
        data['name'] = ''
        response = self.registration.post('/registration', data=data)
        self.assertEqual(response.status_code, 200)

    def test_address(self):
        data['address'] = ''
        response = self.registration.post('/registration', data=data)
        self.assertEqual(response.status_code, 200)

    def test_index1(self):
        data['index'] = ''
        response = self.registration.post('/registration', data=data)
        self.assertEqual(response.status_code, 200)

    def test_index2(self):
        data['index'] = '-2'
        response = self.registration.post('/registration', data=data)
        self.assertEqual(response.status_code, 200)

    def test_comment(self):
        data['comment'] = ''
        response = self.registration.post('/registration', data=data)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
