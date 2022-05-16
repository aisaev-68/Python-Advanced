from typing import TextIO


class Open(object):
    def __init__(self, file, flag, type_errors) -> None:
        self.file = file
        self.flag = flag
        self.type_err = type_errors

    def __enter__(self) -> TextIO:
        self.fp = open(self.file, self.flag)
        return self.fp

    def __exit__(self, exp_type, exp_value, exp_tr) -> bool:
        if exp_type in self.type_err:
            self.fp.close()
            return True
        self.fp.close()


if __name__ == '__main__':
    type_error = (StopIteration, StopAsyncIteration, ArithmeticError, AssertionError, AttributeError, BufferError, EOFError,
                      ImportError, LookupError, MemoryError, NameError, OSError, ReferenceError, RuntimeError, SyntaxError, SystemError,
                      TypeError, ValueError)
    with Open("asd.txt", "w", type_error) as fp:
        fp.write(12)





