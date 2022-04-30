"""
Реализуйте endpoint, с url, начинающийся с  /max_number ,
в который можно будет передать список чисел, перечисленных через / .
Endpoint должен вернуть текст "Максимальное переданное число {number}",
где number, соответственно, максимальное переданное в endpoint число,
выделенное курсивом.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/max_number/...")
def max_number():
    """Put your code here"""


if __name__ == "__main__":
    app.run(debug=True)
