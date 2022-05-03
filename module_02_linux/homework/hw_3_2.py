"""
Давайте напишем свое приложение для учета финансов.
Оно должно уметь запоминать, сколько денег мы потратили за день,
    а также показывать затраты за отдельный месяц и за целый год.

Модифицируйте  приведенный ниже код так, чтобы у нас получилось 3 endpoint:
/add/<date>/<int:number> - endpoint, который сохраняет информацию о совершённой за какой-то день трате денег (в рублях, предполагаем что без копеек)
/calculate/<int:year> -- возвращает суммарные траты за указанный год
/calculate/<int:year>/<int:month> -- возвращает суммарную трату за указанный месяц

Гарантируется, что дата для /add/ endpoint передаётся в формате
YYYYMMDD , где YYYY -- год, MM -- месяц (число от 1 до 12), DD -- число (от 01 до 31)
Гарантируется, что переданная дата -- корректная (никаких 31 февраля)
"""
import datetime
from flask import Flask

app = Flask(__name__)

storage = {}


@app.route("/add/<date>/<int:number>")
def add(date: str, number: int):
    dt = datetime.datetime.strptime(date, '%Y%m%d').date()
    if not storage.get(str(date)):
        storage[str(date)] = number
    else:
        storage[str(date)] += number
    return f'Расходы на {dt}: {number}'


@app.route("/calculate/<int:year>")
def calculate_year(year: int):
    year_dict = dict(filter(lambda val: int(val[0][:4]) == year, storage.items()))
    sum_money = sum(year_dict.values())
    return f'Суммарные траты за {str(year)} год: {str(sum_money)}'


@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year: int, month: int):
    year_dict = dict(filter(lambda val: int(val[0][:4]) == year and int(val[0][4:6]) == month, storage.items()))
    sum_money = sum(year_dict.values())
    return f'Суммарные траты за {str(month)}-й месяц {str(year)} года: {str(sum_money)}'


if __name__ == "__main__":
    app.run(debug=True)
