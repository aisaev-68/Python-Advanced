"""
В 20NN году оккультному автосалону "Чёртово колесо" исполняется ровно 13 лет.
    В честь этого они предлагает своим клиентам уникальную акцию:
    если вы обращаетесь в автосалон в пятницу тринадцатое и ваш автомобиль
    чёрного цвета и марки "Лада" или "BMW", то вы можете поменять колёса со скидкой 13%.
Младший менеджер "Чёртова колеса" слил данные клиентов в интернет,
    поэтому мы можем посчитать, как много клиентов автосалона могли воспользоваться
    скидкой (если бы они об этом знали). Давайте сделаем это!

Реализуйте функцию, c именем get_number_of_luckers которая принимает на вход курсор и номер месяца,
    и в ответ возвращает число клиентов, которые могли бы воспользоваться скидкой автосалона.
    Таблица с данными называется `table_occult_car_repair`
"""

import sqlite3


def get_number_of_luckers(c: sqlite3.Cursor, numb_month: str):
    sql_select = """
    SELECT *
    FROM `table_occult_car_repair`
    WHERE STRFTIME('%m',datetime(timestamp)) = ?
    AND STRFTIME('%d',datetime(timestamp)) = '13'
    AND datetime(timestamp) IN (
    SELECT datetime(timestamp, 'weekday 5')
    FROM `table_occult_car_repair`
    WHERE car_colour = 'чёрный'
    AND (car_type = 'BMW' or car_type = 'Лада'))
    """
    c.execute(sql_select, (numb_month,))
    count = len(c.fetchall())
    return count


if __name__ == "__main__":
    with sqlite3.connect("hw.db") as connection:
        cursor = connection.cursor()
        try:
            numb = int(input('Введите номер месяца:\n>>'))
            if numb < 10:
                numb = '0' + str(numb)
            else:
                numb = str(numb)
            print('Число клиентов, которые могли бы воспользоваться скидкой автосалона равна ',
                  get_number_of_luckers(cursor, numb))
        except ValueError as er:
            print('Введите число.')
