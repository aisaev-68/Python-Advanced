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
        WHERE id in (
        select a.employee_id
        from `table_friendship_schedule` a
        where strftime('%w', a.date) =  ?)
        """
        c.execute(sql_update, (week, ind))


if __name__ == "__main__":

    with sqlite3.connect("hw.db") as connection:
        cursor = connection.cursor()
        update_work_schedule(cursor)

#вариант предложенный преподавателем
# import datetime
# import sqlite3
#
#
# SPORTS_IN_DAYS = {
#     0: "футбол",
#     1: "хоккей",
#     2: "шахматы",
#     3: "SUP сёрфинг",
#     4: "бокс",
#     5: "Dota2",
#     6: "шах-бокс",
# }
#
# get_all_people_id_sport = """
# SELECT id, preferable_sport
#     FROM `table_friendship_employees`
# """
#
# delete_all_query = """
# DELETE FROM `table_work_schedule`;
# """
#
# create_table_query = """
# CREATE TABLE IF NOT EXISTS `table_work_schedule` (
#     employee_id INTEGER NOT NULL,
#     date TEXT NOT NULL
# );
# """
#
# insert_schedule_query = """
# INSERT INTO `table_work_schedule`
#     (employee_id, date)
#     VALUES (?, ?)
# """
#
#
# def update_work_schedule(c: sqlite3.Cursor) -> None:
#     c.execute(create_table_query)
#     c.execute(delete_all_query)
#
#     c.execute(get_all_people_id_sport)
#     all_people = c.fetchall()
#
#     start_day = datetime.datetime(2020, 1, 1)
#     person_start_key = 0
#     all_people_count = len(all_people)
#
#     for i_day in range(366):
#         current_day = start_day + datetime.timedelta(days=i_day)
#         count_work_shift = 0
#         count = 0
#         while count_work_shift < 10:
#             person_key = (person_start_key + count) % all_people_count
#             i_person = all_people[person_key]
#
#             if SPORTS_IN_DAYS[current_day.weekday()] != i_person[1]:
#                 c.execute(insert_schedule_query, (i_person[0], current_day.strftime("%Y-%m-%d")))
#                 count_work_shift += 1
#             count += 1
#         person_start_key += 1
#
#
# if __name__ == "__main__":
#     with sqlite3.connect("hw.db") as connection:
#         cursor = connection.cursor()
#         update_work_schedule(cursor)