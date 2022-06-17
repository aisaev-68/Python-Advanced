"""
На заводе "Дружба" работает очень дружный коллектив.
Рабочие работают посменно, в смене -- 10 человек.
На смену заходит 366 .

Бухгалтер завода составила расписание смен и занесла его в базу данных
    в таблицу `table_work_schedule`, но совершенно не учла тот факт,
    что все сотрудники люди спортивные и ходят на различные спортивные кружки:
        1. футбол (проходит по понедельникам)
        2. хоккей (по вторникам
        3. шахматы (среды)
        4. SUP сёрфинг (четверг)
        5. бокс (пятница)
        6. Dota2 (суббота)
        7. шах-бокс (воскресенье)

        Dota2,47
        SUP сёрфинг,67
        бокс,46
        футбол,51
        хоккей,48
        шах-бокс,48
        шахматы,59

Как вы видите, тренировки по этим видам спорта проходят в определённый день недели.

Пожалуйста помогите изменить расписание смен с учётом личных предпочтений коллектива
    (или докажите, что то, чего они хотят - не возможно).
"""
import sqlite3


def update_work_schedule(c: sqlite3.Cursor) -> None:
    week_lst = ['шах-бокс', 'футбол', 'хоккей', 'шахматы', 'SUP сёрфинг', 'бокс', 'Dota2', ]

    for ind, week in enumerate(week_lst):
        sql_update = f"""
        UPDATE `table_friendship_employees`
        SET preferable_sport = ?
        WHERE name in (
        select b.name
        from `table_friendship_schedule` a,
        `table_friendship_employees` b
        where a.employee_id = b.id and date in
        (SELECT date(c.date, 'weekday {ind}')
        FROM `table_friendship_schedule` c))
        """
        c.execute(sql_update, (week,))


if __name__ == "__main__":

    with sqlite3.connect("hw.db") as connection:
        cursor = connection.cursor()
        update_work_schedule(cursor)
        sql_select_group = """
        SELECT preferable_sport, COUNT(*) 
        FROM `table_friendship_employees` 
        GROUP BY preferable_sport
        """
        cursor.execute(sql_select_group)
        data = cursor.fetchall()
        if len(data) == 7:
            print('Все данные обновлены')
        else:
            print('Данные обновлены только по значению Dota2, чего они хотят - не возможно')
