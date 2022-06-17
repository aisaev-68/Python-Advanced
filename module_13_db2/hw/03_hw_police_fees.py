"""
Вы работаете программистом в IT отделе ГИБДД.
    Ваш отдел отвечает за обслуживание камер,
    которые фиксируют превышения скорости и выписывают автоматические штрафы.
За последний месяц к вам пришло больше тысячи жалоб на ошибочно назначенные штрафы,
    из которых около 100 были признаны и правда ошибочными.

Список из дат и номеров автомобилей ошибочных штрафов прилагается к заданию,
    пожалуйста удалите записи об этих штрафах из таблицы `table_fees`
"""


import sqlite3


def read_csv(file) -> list:
    with open(file, 'r', encoding='utf-8') as f:
        read_csv = f.readlines()[1:]

    tuples = []
    for row in read_csv:
        tuples.append(tuple(row.split()))
    return tuples


def select_quest(c: sqlite3.Cursor, data: tuple):
    sql_select_request = """
    SELECT COUNT(*)  
    FROM `table_fees` 
    WHERE  timestamp = ? 
    AND truck_number = ?
    """
    c.execute(sql_select_request, data)
    count = c.fetchone()[0]
    if count:
        return True
    else:
        return False


def delete_wrong_fees(c: sqlite3.Cursor, wrong_fees_file: str) -> None:
    sqlite_delete_query = """DELETE from `table_fees` 
    where timestamp = ? AND truck_number = ?
    """
    lst = read_csv(wrong_fees_file)
    count = 0
    for data_tuple in lst:
        numb, time_stamp = data_tuple[0].split(',')
        if select_quest(c, (time_stamp, numb,)):
            c.execute(sqlite_delete_query, (time_stamp, numb,))
            count += 1
        else:
            print('Данные {} отсутствуют в базе {}'.format(data_tuple, 'table_fees'))
    print("Удалено записей:", count)


if __name__ == "__main__":
    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()

        delete_wrong_fees(cursor, "wrong_fees.csv")
