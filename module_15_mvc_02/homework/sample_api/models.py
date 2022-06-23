import sqlite3


# class Hotels:
#     def __init__(self, id_room: int, floor: int, quest_num: int, beds: int, price: int):
#         self.id_room = id_room
#         self.floor = floor
#         self.guest_num = quest_num
#         self.beds = beds
#         self.price = price
#
#     def __getitem__(self, item):
#         return getattr(self, item)


def init_db() -> None:
    with sqlite3.connect('table_hotels.db') as conn:
        cursor = conn.cursor()

        cursor.executescript(
            'CREATE TABLE IF NOT EXISTS `table_rooms` '
            '(id_room INTEGER PRIMARY KEY AUTOINCREMENT, floor INTEGER, beds INTEGER,'
            'guest_num INTEGER, price INTEGER)'

        )

        cursor.executescript(
            'CREATE TABLE IF NOT EXISTS `table_booking` '
            '(id INTEGER PRIMARY KEY AUTOINCREMENT, id_room INTEGER,'
            'firstname TEXT, lastname TEXT, check_in TEXT, check_out TEXT)'
        )


def get_all_rooms() -> list:
    with sqlite3.connect('table_hotels.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * from `table_rooms`')
        all_rooms = cursor.fetchall()

        return all_rooms


def add_room_db(value: tuple) -> None:
    with sqlite3.connect('table_hotels.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO `table_rooms` '
            '(floor, beds, guest_num, price) VALUES (?, ?, ?, ?)',
            value
        )


def get_room_booking(value: tuple) -> list:
    with sqlite3.connect('table_hotels.db') as conn:
        cursor = conn.cursor()

        cursor.execute('SELECT * '
                       'FROM `table_rooms` '
                       'WHERE guest_num = ? AND id_room IN (SELECT id_room FROM `table_booking` '
                       'WHERE check_in = ? AND check_out = ?)', value)
        data = cursor.fetchall()

        room_request = []
        for row in data:
            room_request.append({"roomId": row[0],
                                 "floor": row[1],
                                 "guestNum": row[2],
                                 "beds": row[3],
                                 "price": row[4]})
        return room_request


def add_booking(value: tuple) -> bool:
    with sqlite3.connect('table_hotels.db') as conn:
        cursor = conn.cursor()
        if cursor.execute(
            'INSERT INTO `table_booking` '
            '(id_room, firstname, lastname, check_in, check_out) VALUES (?, ?, ?, ?, ?)',
            value
        ):
            return True
        else:
            return False


# def get_room_id(id: int) -> list:
#     with sqlite3.connect('table_hotels.db') as conn:
#         cursor = conn.cursor()
#         cursor.execute('SELECT id_room from `table_booking`'
#                        'WHERE id_room = ?', (id,))
#         count_room = cursor.fetchall()
#         id_list = []
#         for raw in count_room:
#             id_list.append(raw[0])
#
#         return id_list
def get_room_id() -> list:
    with sqlite3.connect('table_hotels.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id_room from `table_rooms`'
                       'WHERE id_room NOT IN ('
                       'SELECT id_room FROM `table_booking`)')
        count_room = cursor.fetchall()
        id_list = []
        for raw in count_room:
            id_list.append(raw[0])

        return id_list

