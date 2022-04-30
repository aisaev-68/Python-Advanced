"""
Напишите  hello-world endpoint , который возвращал бы строку "Привет, <имя>. Хорошей пятницы!".
Вместо хорошей пятницы, endpoint должен уметь желать хорошего дня недели в целом, на русском языке.
Текущий день недели можно узнать вот так:
>>> import datetime
>>> print(datetime.datetime.today().weekday())
"""

import datetime

from flask import Flask

app = Flask(__name__)


@app.route("/hello-world/...")
def hello_world() -> str:
    """Put your code here"""


if __name__ == "__main__":
    app.run(debug=True)
