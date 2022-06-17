"""
Пожалуйста, запустите скрипт generate_hw_database.py прежде, чем приступать к выполнению практической работы.
После выполнения скрипта у вас должен появиться файл базы hw.db и в нем таблица table_truck_with_vaccine
Грузовик перевозит очень важную вакцину.

Условия хранения этой вакцины весьма необычные -- в отсеке должна быть температура  -18±2 градуса.
    Если температурный режим был нарушен - вакцина считается испорченной.

Для проверки состояния вакцины применяется датчик, который раз в час измеряет температуру внутри контейнера.
    Если в контейнере было хотя бы 3 часа с температурой, которая находится вне указанного выше диапазона -
    температурный режим считается нарушенным.

Пожалуйста, реализуйте функцию `check_if_vaccine_has_spoiled`,
    которая по номеру грузовика определяет, не испортилась ли вакцина.
"""
import sqlite3


def check_if_vaccine_has_spoiled(
        c: sqlite3.Cursor,
        truck_number: str,
) -> bool:
    sql_request = """
    SELECT COUNT(*)  
    FROM `table_truck_with_vaccine` 
    WHERE  NOT temperature_in_celsius between 16 AND 20 
    AND truck_number = ?
    """
    c.execute(sql_request, [(truck_number)])
    count = c.fetchone()[0]
    if count:
        return True
    else:
        return False


if __name__ == '__main__':
    with sqlite3.connect('hw.db') as conn:
        cur = conn.cursor()
        numb = input('Введите номер грузовика:\n>>')

        if check_if_vaccine_has_spoiled(cur, numb):
            print('Вакцина на грузовие {} испортилась'.format(numb))
        else:
            print('Вакцина на грузовие {} не испортилась'.format(numb))
