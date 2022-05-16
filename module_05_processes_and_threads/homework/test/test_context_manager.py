import sys
import unittest
import io

from ..context_manager import Open


class TestStreamsOpen(unittest.TestCase):
    def setUp(self):
        self.type_error = (
            StopIteration, StopAsyncIteration, ArithmeticError, AssertionError, AttributeError, BufferError, EOFError,
            ImportError, LookupError, MemoryError, NameError, OSError, ReferenceError, RuntimeError, SyntaxError,
            SystemError, TypeError, ValueError)

    def test_streams_open(self):
        with self.assertRaises(AssertionError):
            with self.assertRaises(Exception):
                with Open("asd.txt", "w", self.type_error) as fp:
                    fp.write(12)


if __name__ == '__main__':
    unittest.main()
