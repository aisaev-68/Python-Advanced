import sqlite3


def read_data():
    with open('hw_1.md', 'r', encoding='utf-8') as file:
        for line in file.readlines():
            data = line.replace('принадлежит', '').replace('описание:', '').replace('"', '').replace('`', '')
            if len(data) > 0 and data[:1].isdigit():
                lst.append(tuple(data[4:].split(',', 3)))


def select(surname: str, name: str, patronymic: str) -> list:
    with sqlite3.connect("hw_1_database.db") as conn:
        cursor = conn.cursor()
        sql = "SELECT * FROM table_people WHERE name LIKE ? AND name LIKE ? AND name LIKE ?"
        cursor.execute(sql, [(surname + '%'), '%' + name + '%', '%' + patronymic + "%"])
        result = cursor.fetchall()
    return result


def insert(sql: str, value: tuple):
    with sqlite3.connect("hw_1_database.db") as conn:
        cursor = conn.cursor()
        cursor.execute(sql, value)
        conn.commit()


def main(data_tuple: tuple):
    surname = data_tuple[2].strip().split(' ')[0]
    firstname = data_tuple[2].strip().split(' ')[1][:1]
    patronymic = data_tuple[2].strip().split(' ')[1][2:3]
    res = select(surname, firstname, patronymic)
    if res:
        if 6 <= len(data_tuple[0].strip()) <= 9:
            value_data_car = (data_tuple[0].strip(), data_tuple[1].strip(), data_tuple[3].strip(), res[0][0])
            sql = "INSERT INTO table_car VALUES(?, ?, ?, ?);"
            insert(sql, value_data_car)
        else:
            print(
                f'Длина государственного регистрационного знака {data_tuple[0].strip()}'
                f' не может быть меньше 6 и больше 9')
    else:
        value_data_people = (1900, data_tuple[2].strip())
        sql1 = "INSERT INTO table_people(birth_year, name) VALUES(?, ?);"
        insert(sql1, value_data_people)
        res_people = select(surname, firstname, patronymic)
        value_data_car = (data_tuple[0].strip(), data_tuple[1].strip(), data_tuple[3].strip(), res_people[0][0])
        sql2 = "INSERT INTO table_car VALUES(?, ?, ?, ?);"
        insert(sql2, value_data_car)


if __name__ == "__main__":
    lst = []
    read_data()
    for data_line in lst:
        main(data_line)
