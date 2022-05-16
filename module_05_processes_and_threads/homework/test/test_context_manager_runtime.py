import unittest
from io import StringIO

from ..context_manager_runtime import Write


def division_function(dividend, divisor):
    print(dividend / divisor)


class TestStreamsWrite(unittest.TestCase):
    def setUp(self):
        self.stdout_stream = StringIO()
        self.stderr_stream = StringIO()

    def test_streams_write(self):
        with Write(self.stdout_stream, self.stderr_stream):
            with self.assertRaises(Exception):
                print('TEXT stdout')
                print(5 / 0)


if __name__ == '__main__':
    unittest.main()
