"""
Иван Совин - эффективный менеджер.
Когда к нему приходит сотрудник просить повышение з/п -
    Иван может повысить её только на 10%.

Если после повышения з/п сотрудника будет больше з/п самого
    Ивана Совина - сотрудника увольняют, в противном случае з/п
    сотрудника повышают.

Давайте поможем Ивану стать ещё эффективнее,
    автоматизировав его нелёгкий труд.
    Пожалуйста реализуйте функцию которая по имени сотрудника
    либо повышает ему з/п, либо увольняет сотрудника
    (удаляет запись о нём из БД).

Таблица с данными называется `table_effective_manager`
"""
import sqlite3


def ivan_sovin_the_most_effective(
        c: sqlite3.Cursor,
        name: str,
) -> None:
    c.execute("""SELECT * FROM `table_effective_manager`'
              'WHERE  name = 'Иван Совин'""")
    ivan_salary = c.fetchall()[0][2]

    sql_select = """
    SELECT *  
    FROM `table_effective_manager`  
    WHERE  name LIKE ? 
    """
    c.execute(sql_select, (name + '%',))
    data = c.fetchall()[0][2]

    salary = int(data * 1.1)
    if salary > ivan_salary:
        sql_delete = """DELETE from `table_effective_manager`  
        where name = ?
        """
        c.execute(sql_delete, (name,))
        print(f'{name} уволен')
    else:
        sql_update_salary = """
        UPDATE `table_effective_manager` SET salary = ?
        WHERE name = ?
        """
        c.execute(sql_update_salary, (salary, name))
        print(f'{name} зарплата повышена до {salary}')


if __name__ == "__main__":
    with sqlite3.connect("hw.db") as connection:
        cursor = connection.cursor()
        name_personal = input('Введите имя сотрудника (Фамилия и инициалы): ').title()
        ivan_sovin_the_most_effective(cursor, name_personal)
