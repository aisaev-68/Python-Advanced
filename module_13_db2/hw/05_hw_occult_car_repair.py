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
    AND strftime('%w', timestamp) =  '5'
    AND car_colour = 'чёрный'
    AND (car_type = 'BMW' or car_type = 'Лада')
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

#метод предложенный преподавателем
# import datetime
# import sqlite3
#
# get_auto_by_month_color_type_query = """
# SELECT COUNT(*)
#     FROM `table_occult_car_repair`
#     WHERE timestamp LIKE ? AND
#         car_colour = ? AND
#         (car_type = ? OR car_type = ?)
# """
#
#
# def get_number_of_lucky(c: sqlite3.Cursor, month: int):
#     #  Для добавления ведущих нулей к строке лучше использовать
#     #  метод zfill строковых объектов.
#     # month_str = f"0{month}" if month < 10 else f"{month}"
#     timestamp = f"2020-{str(month).zfill(2)}-13"
#
#     if datetime.datetime.strptime(timestamp, "%Y-%m-%d").weekday() == 4:
#         c.execute(
#             get_auto_by_month_color_type_query,
#             (timestamp + "%", "чёрный", "BMW", "Лада")
#         )
#         return cursor.fetchone()[0]
#     return 0
#
#
# MONTHS = (
#     "January",
#     "February",
#     "March",
#     "April",
#     "May",
#     "June",
#     "July",
#     "August",
#     "September",
#     "October",
#     "November",
#     "December"
# )
#
#
# if __name__ == "__main__":
#     with sqlite3.connect("hw.db") as conn:
#         cursor = conn.cursor()
#
#         for i in range(1, 13):
#             autos_count = get_number_of_lucky(cursor, i)
#             print(f"In {MONTHS[i - 1]} there {autos_count} cars.")
