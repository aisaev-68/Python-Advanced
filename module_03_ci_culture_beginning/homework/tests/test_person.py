import unittest
import datetime

from ..person import Person


class TestPerson(unittest.TestCase):

    def setUp(self):
        self.new_person = Person('Mark', 1987)

    def test_name(self):
        self.assertEqual(self.new_person.get_name(), 'Mark')

    def test_age(self):
        self.assertEqual(self.new_person.get_age(), 1987 - datetime.datetime.now().year)

    def test_address(self):
        self.assertEqual(self.new_person.get_address(), '')

    def test_homeless(self):
        self.assertFalse(self.new_person.is_homeless())

    def test_set_address(self):
        self.new_person.set_address('Moscow')
        self.assertEqual(self.new_person.get_address(), 'Moscow')

    def test_set_name(self):
        self.new_person.set_name('Tom')
        self.assertEqual(self.new_person.get_name(), 'Tom')



if __name__ == '__main__':
   unittest.main(verbosity=2)

