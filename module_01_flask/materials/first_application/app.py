import datetime
from flask import Flask

app = Flask(__name__)
count = 0


@app.route('/test')
def test_function():
    return 'Это тестовая страничка, ответ сгенерирован в %s' % \
           datetime.datetime.now().utcnow()


@app.route('/hello/world')
def test_hello():
    return 'Hello, world!'


@app.route('/counter')
def test_count():
    global count
    count += 1
    return f'Количество посещений сайта: {count}'
