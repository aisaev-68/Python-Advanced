import datetime
import random
from flask import Flask

app = Flask(__name__)


@app.route('/hello_world')
def test_function():
   return 'Привет, мир!'


@app.route('/cars')
def test_cars():
   return 'Chevrolet, Renault, Ford, Lada'


@app.route('/cats')
def test_cats():
   return random.choice(['Корниш рекс', 'Русская голубая', 'Шотландская вислоухая', 'Мэйн-Кун', 'Манчкин'])


@app.route('/get_time/now')
def test_time():
   return f'Точное время: {datetime.datetime.now()}'


@app.route('/get_time/future')
def test_future():
   today = datetime.datetime.now()
   current_time_after_hour = today + datetime.timedelta(hours=1)
   return f'Точное время через час будет {current_time_after_hour}'


@app.route('/get_random_word')
def test_word():
   with open("war_and_peace.txt", "r", encoding='utf-8') as file:
      txt = file.read()
      words = list(map(str, txt.split()))
      return f'Случайное слово из книги Война и Мир Льва Толстого: {random.choice(words)}'

