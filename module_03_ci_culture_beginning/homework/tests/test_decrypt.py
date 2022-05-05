import unittest

from ..decrypt import decrypt

class TestDecrypt(unittest.TestCase):
    def setUp(self) -> None:
        self.crypt_lst = ['абра-кадабра.', 'абраа..-кадабра', 'абраа..-.кадабра', 'абра--..кадабра', 'абрау...-кадабра',
                     'абра........', 'абр......a.', '1..2.3', '.', '1.......................']
        self.decrypt_lst = ['абра-кадабра', 'абра-кадабра', 'абра-кадабра', 'абра-кадабра', 'абра-кадабра',
                       '', 'a', '23', '', '']

    def test_decrypt(self):
        for index, item in enumerate(self.crypt_lst):
            self.assertEqual(decrypt(item), self.decrypt_lst[index])

if __name__ == '__main__':
    unittest.main()