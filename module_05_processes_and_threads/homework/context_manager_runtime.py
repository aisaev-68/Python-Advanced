import sys
import traceback
from typing import TextIO


class Write:
    def __init__(self, stdout: TextIO, stderr: TextIO) -> None:
        self.stdout = stdout
        self.stderr = stderr

    def __enter__(self) -> None:
        sys.stdout = self.stdout
        sys.stderr = self.stderr

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type:
            traceback.print_exception(exc_type, exc_val, exc_tb, limit=None, file=self.stderr)


if __name__ == '__main__':
    with open('stdout.txt', 'a', encoding='utf-8') as stdout:
        with open('stderr.txt', 'a', encoding='utf-8') as stderr:
            with Write(stdout, stderr):
                print('ТЕКСТ stdout')
                print(7 / 0)
