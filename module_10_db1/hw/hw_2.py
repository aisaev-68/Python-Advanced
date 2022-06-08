import sqlite3


def select(sql: str, value: str) -> list:
    with sqlite3.connect("hw_2_database.db") as conn:
        cursor = conn.cursor()
        if value:
            cursor.execute(sql, [(int(value))])
        else:
            cursor.execute(sql)
        result = cursor.fetchall()
    return result


if __name__ == "__main__":
    sql_poor_people = "SELECT COUNT(*) FROM salaries WHERE salary < ?"
    poor_peoples_wages = '5000'
    number_persons = select(sql_poor_people, poor_peoples_wages)[0][0]
    number_rich_people = int(number_persons * 0.1)
    print('1. За чертой бедности - т.е. получает меньше 5.000 гульденов в год ',
          str(number_persons), ' человек.')

    sql_average_salary = "SELECT AVG(salary) FROM salaries"
    print('2. Средняя заработную плату по острову N в гульденах - ',
          str(select(sql_average_salary, '')[0][0]))

    sql_numbers_people = "SELECT COUNT(*) FROM salaries ORDER BY salary DESC"
    number_peoples = select(sql_numbers_people, '')[0][0]
    number_sad_peoples = int(number_peoples) - number_rich_people
    sql_rich_people = "SELECT SUM(salary) FROM (SELECT * FROM salaries " \
                      "ORDER BY salary DESC LIMIT ?)"
    sum_rich_people = select(sql_rich_people, str(number_rich_people))[0][0]
    if int(number_peoples) % 2 == 0:
        med_people = int(number_peoples) / 2
        sql_median_salary = f"SELECT AVG(salary) FROM (SELECT * FROM salaries " \
                            f"ORDER BY salary DESC LIMIT {med_people}, 2)"
    else:
        med_people = int(number_peoples / 2) + 1
        sql_median_salary = f"SELECT AVG(salary) FROM (SELECT * FROM salaries " \
                            f"ORDER BY salary DESC LIMIT {med_people}, 1)"
    median_salary = select(sql_median_salary, '')
    print('3. Медианная з/п острова равна ', str(median_salary))

    sql_sad_peoples = "SELECT SUM(salary) FROM (SELECT * FROM salaries ORDER BY salary ASC LIMIT ?)"
    sum_sad_peoples = select(sql_sad_peoples, str(number_sad_peoples))[0][0]

    print('4. Число социального неравенства F, определяемое как F = T/K равна ', str(sum_rich_people / sum_sad_peoples))
