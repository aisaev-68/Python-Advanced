import sqlite3

sql_request = """
SELECT COUNT(*)
    FROM `table_stars`
    WHERE constellation = ?
"""


def get_stars_count_by_constellation(
        c: sqlite3.Cursor,
        constellation_name: str,
) -> int:
    c.execute(sql_request, (constellation_name,))
    request_result, *_ = c.fetchone()

    return request_result


if __name__ == "__main__":
    with sqlite3.connect("db_stars.db") as conn:
        cursor = conn.cursor()

        name = input("Введите имя созвездия\n> ")

        stars_count = get_stars_count_by_constellation(cursor, name.lower())

        print(
                "В созвездии {name} к-во звёзд в БД: {count}".format(
                        name=name, count=stars_count
                )
        )
