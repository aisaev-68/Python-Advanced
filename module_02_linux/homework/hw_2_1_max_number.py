"""
Реализуйте endpoint, с url, начинающийся с  /max_number ,
в который можно будет передать список чисел, перечисленных через / .
Endpoint должен вернуть текст "Максимальное переданное число {number}",
где number, соответственно, максимальное переданное в endpoint число,
выделенное курсивом.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/max_number/<path:numbers>")
def max_number(numbers:str) -> str:
    number = numbers.split('/')
    numb_list = []
    for nums in number:
        numb_list.append(int(nums))
    return f'Максимальное переданное число <i>{max(numb_list)}</i>'


if __name__ == "__main__":
    app.run(debug=True)
