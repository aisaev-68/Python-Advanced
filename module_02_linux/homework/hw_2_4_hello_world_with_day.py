"""
Напишите  hello-world endpoint , который возвращал бы строку "Привет, <имя>. Хорошей пятницы!".
Вместо хорошей пятницы, endpoint должен уметь желать хорошего дня недели в целом, на русском языке.
Текущий день недели можно узнать вот так:

"""

import datetime

from flask import Flask

app = Flask(__name__)


@app.route("/hello-world/<string:name>")
def hello_world(name: str) -> str:
    if datetime.datetime.today().weekday() == 0:
         return f'Привет, {name}. Хорошего понедельника'
    elif datetime.datetime.today().weekday() == 1:
        return f'Привет, {name}. Хорошего вторника'
    elif datetime.datetime.today().weekday() == 2:
        return f'Привет, {name}. Хорошей среды'
    elif datetime.datetime.today().weekday() == 3:
        return f'Привет, {name}. Хорошего четверга'
    elif datetime.datetime.today().weekday() == 4:
        return f'Привет, {name}. Хорошей пятницы'
    elif datetime.datetime.today().weekday() == 5:
        return f'Привет, {name}. Хорошей субботы'
    elif datetime.datetime.today().weekday() == 6:
        return f'Привет, {name}. Хорошего воскресенья'


if __name__ == "__main__":
    app.run(debug=True)
