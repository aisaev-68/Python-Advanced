import unittest
import datetime

from ..hw_3_2 import app

storage_dct = {'20210123': 3000, '20210124': 3000, '20220504': 1000, '20220505': 240, '20220601': 2000}


class TestCalculate(unittest.TestCase):
    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def test_add(self):
        self.base_url = '/add/'
        for key, value in storage_dct.items():
            response = self.app.get(self.base_url + key + '/' + str(value))
            response_text = response.data.decode()
            self.assertEqual(('').join(response_text.split()[2][:-1].split('-')), key)
            self.assertEqual(int(response_text.split()[3]), value)

    def test_calculate_year(self):
        self.base_url = '/calculate/'
        for key in storage_dct.keys():
            year_dict = {key1: value1 for key1, value1 in storage_dct.items() if int(key1[:4]) == int(key[:4])}
            sum_money = sum(year_dict.values())
            response = self.app.get(self.base_url + key[:4])
            response_text = response.data.decode()
            self.assertEqual(int(response_text.split()[3]), int(key[:4]))
            self.assertEqual(int(response_text.split()[5]), int(sum_money))

    def test_calculate_month(self):
        self.base_url = '/calculate/'

        for key in storage_dct.keys():
            year_dict = {key1: value1 for key1, value1 in storage_dct.items() if int(key1[:6]) == int(key[:6])}
            sum_money = sum(year_dict.values())
            response = self.app.get(self.base_url + key[:4] + '/' + key[4:6])
            response_text = response.data.decode()
            self.assertEqual(int(response_text.split()[5]), int(key[:4]))
            self.assertEqual(int(response_text.split()[3][:1]), int(key[4:6]))
            self.assertEqual(int(response_text.split()[7]), int(sum_money))


if __name__ == '__main__':
    unittest.main()
