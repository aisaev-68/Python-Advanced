import datetime

class Person:
    def __init__(self, name: str, year_of_birth: int, address: str = '') -> None:
        self.name = name
        self.yob = year_of_birth
        self.address = address

    def get_age(self) -> int:
        now = datetime.datetime.now()
        return self.yob - now.year

    def get_name(self) -> str:
        return self.name

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address

    def is_homeless(self):
        '''
        returns True if address is not set, false in other case
        '''
        return self.address is None

