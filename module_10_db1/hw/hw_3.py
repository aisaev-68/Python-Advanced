import sqlite3


def select(sql_str: str) -> list:
    with sqlite3.connect("hw_3_database.db") as conn:
        cursor = conn.cursor()
        cursor.execute(sql_str)
        result = cursor.fetchall()
    return result


if __name__ == "__main__":
    sql = "SELECT COUNT(*) FROM table_1"
    print('В таблице table_1 хранятся', select(sql)[0][0], 'записей.')

    sql = "SELECT COUNT(*) FROM table_2"
    print('В таблице table_2 хранятся', select(sql)[0][0], 'записей.')

    sql = "SELECT COUNT(*) FROM table_3"
    print('В таблице table_3 хранятся', select(sql)[0][0], 'записей.')

    sql = "SELECT COUNT(DISTINCT id + value) FROM table_1"
    print('В таблице table_1 хранятся', select(sql)[0][0], 'уникальных записей.')

    sql = "SELECT count(*) FROM table_1 JOIN table_2 ON (table_2.id =table_1.id and table_2.value =table_1.value)"
    print('Из таблице table_1', select(sql)[0][0], 'записей встручаются в таблице table_2.')

    sql = "SELECT count(*) FROM table_1 JOIN table_2 ON (table_2.id =table_1.id and " \
          "table_2.value =table_1.value) JOIN table_3 ON (table_3.id =table_1.id and table_3.value =table_1.value)"
    print('Из таблице table_1', select(sql)[0][0], 'записей встречаются в table_2 и table_3')