import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/test')
def test_function():
   return 'Это тестовая страничка, ответ сгенерирован в %s' % \
                     datetime.datetime.now().utcnow()
