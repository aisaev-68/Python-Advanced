####Ошибки сгенерированные test_person.py для модуля person.py

1. Выполнение модуля get_age()

        def get_age(self):
           now = datetime.datetime.now()
          return self.yob - now.year>
 	
    вызывает следующую ошибку

        NameError: name 'datetime' is not defined

    Необходимо подключить библиотеку

        import datetime

2. Выполнение модуля set_name()

        def set_name(self, name):
          self.name = self.name

    вызывает следующую ошибку

       Tom != Mark
    
       Expected :Mark
       Actual   :Tom
       <Click to see difference>

       Traceback (most recent call last):
         File "/home/aisaev/python_advanced/module_03_ci_culture_beginning/homework/tests/test_person.py", line 30, in test_set_name
            self.assertEqual(self.new_person.get_name(), 'Tom')
       AssertionError: 'Mark' != 'Tom'

    указанный выше код необходимо исправить на

        def set_name(self, name):
          self.name = name

3. Выполнение модуля set_address()

       def set_address(self, address):
         self.address == address

    вызывает следующую ошибку

       Moscow != 

       Expected :
       Actual   :Moscow
       <Click to see difference>

       Traceback (most recent call last):
       File "/home/aisaev/python_advanced/module_03_ci_culture_beginning/homework/tests/test_person.py", line 26, in test_set_address
         self.assertEqual(self.new_person.get_address(), 'Moscow')
       AssertionError: '' != 'Moscow'

    указанный выше код необходимо исправить на

        def set_address(self, address):
          self.address = address