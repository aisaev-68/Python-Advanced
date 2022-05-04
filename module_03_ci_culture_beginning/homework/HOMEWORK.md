 #### Homework Module 03


  1. Мы кое-что забыли проверить, когда писали тест test_can_get_correct_username_with_weekdate: добавьте в тест корректности вернувшегося дня недели

 2. При работе с деньгами нужно все сто раз перепроверить: давайте протестируем наше приложение - калькулятор трат:

    * заполните storage неким изначальным значением, с которым вы будете потом работать в каждом тесте.
    * проверьте, что ендпоинт /add/ работает
    * проверьте, что оба ендпоинта /calculate/ работают
    * проверьте, что ендпоинт /add/ может принять дату только в формате YYYYMMDD и в случае, если вы передаете невалидное значение, то что-то идет не так. В этом задании вам нужно добиться такого условия, когда ендпоинт свалится с ошибкой и вы сможете ее обработать в тесте.
    * проверьте, как будут работать ендпоинты calculate если в storage ничего нет

 3. Добавьте тесты на домашнее задание 3_3 из прошлого модуля. Напишите тесты на все проверки, что есть в задании.

 4. Каждый разработчик еще и тестировщик: он должен уметь покрыть тестами свой код. Но бывает так, что он не успевает, и просит помочь себе в этом деле своего товарища тестировщика. Вот и сейчас так получилось, код есть, но тестами не покрыт. Да и кажется, писался он в попыхах пальцем левой ноги, надо его проверить:

    * покройте данный класс юнит-тестами: все методы должны быть проверены

    * используя юнит тесты найдите ошибки и исправьте их

    * ответ оформите в виде markdown файла -> ERRORS.MD. подсказка по синтаксису: https://github.com/OlgaVlasova/markdown-doc/blob/master/README.md

   ```python

class Person:
    def __init__(self, name, year_of_birth, address=''):
        self.name = name
        self.yob = year_of_birth
        self.address = address

    def get_age(self):
		now = datetime.datetime.now()
		return self.yob - now.year

	def get_name(self):
		return self.name

	def set_name(self, name):
		self.name = self.name

	def set_address(self, address):
		self.address == address

	def get_address(self):
		return self.address

	def is_homeless(self):
		'''
		returns True if address is not set, false in other case
		'''
		return address is None
   ```

