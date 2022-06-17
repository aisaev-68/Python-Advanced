"""
Иногда бывает важно сгенерировать какие то табличные данные по заданным характеристикам.
К примеру, если вы будете работать тестировщиками, вам может потребоваться добавить
    в тестовую БД такой правдоподобный набор данных (покупки за сутки, набор товаров в магазине,
    распределение голосов в онлайн голосовании).

Давайте этим и займёмся!

Представим, что наша FrontEnd команда делает страницу сайта УЕФА с жеребьевкой команд
    по группам на чемпионате Европы.

Условия жеребьёвки такие:
Есть N групп.
В каждую группу попадает 1 "сильная" команда, 1 "слабая" команда и 2 "средние команды".

Задача: написать функцию generate_data, которая на вход принимает количество групп (от 4 до 16ти)
    и генерирует данные, которыми заполняет 2 таблицы:
        1. таблицу со списком команд (столбцы "номер команды", "Название", "страна", "сила команды")
        2. таблицу с результатами жеребьёвки (столбцы "номер команды", "номер группы")

Таблица с данными называется `uefa_commands` и `uefa_draw`
"""


from faker import Faker
import sqlite3

mygen = Faker('ru_RU')


def generate_test_data(c: sqlite3.Cursor, number_of_groups: int) -> None:
    sql_select_group = """
    SELECT *  
    FROM `uefa_draw` 
    ORDER BY command_number DESC LIMIT 1
    """
    c.execute(sql_select_group)
    data = c.fetchall()

    if data:
        max_index = data[0][1]
        max_group = data[0][2]
    else:
        max_group = 0
        max_index = 0

    ind = 0
    for group in range(max_group + 1, max_group + number_of_groups + 1):
        for index, level in enumerate(level_lst):
            club = mygen.company()
            country = mygen.country()

            sql_add_draw = """
                INSERT INTO `uefa_draw` (command_number, group_number)
                VALUES(?, ?)
                """

            c.execute(sql_add_draw, (max_index + ind + 1, group))

            sql_add_commands = """
            INSERT INTO `uefa_commands` (command_number, command_name, command_country, command_level)
            VALUES(?, ?, ?, ?)
            """

            c.execute(sql_add_commands, (max_index + ind + 1, club, country, level))

            ind += 1


if __name__ == "__main__":
    level_lst = ['сильная', 'слабая', 'средняя', 'средняя']
    with sqlite3.connect("hw.db") as connection:
        cursor = connection.cursor()

        try:
            group_numb = int(input('Введите количество групп: '))
            generate_test_data(cursor, group_numb)
            if group_numb % 4 != 0:
                raise Exception
        except ValueError as er:
            print('Введите число 4 или кратное ему.')
