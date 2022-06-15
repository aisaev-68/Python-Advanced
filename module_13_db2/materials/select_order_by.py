import sqlite3

get_all_people_by_class_sql = """
SELECT *
    FROM `table_school`
    WHERE class = ?
    ORDER BY amount_of_money
"""


def get_worst_student_name_by_class_number(
        c: sqlite3.Cursor,
        class_number: int,
) -> str:
    c.execute(get_all_people_by_class_sql, (class_number,))

    student_data = c.fetchone()

    return student_data[1]


if __name__ == "__main__":
    with sqlite3.connect("db_school.db") as conn:
        cursor = conn.cursor()

        worst_student = get_worst_student_name_by_class_number(cursor, 9)

        print(worst_student)
