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


def init_db():
    with sqlite3.connect('table_hotels.db') as conn:
        cursor = conn.cursor()

        cursor.executescript(
            'CREATE TABLE IF NOT EXISTS `table_rooms`'
            '(id_room INTEGER PRIMARY KEY AUTOINCREMENT, floor INTEGER, beds INTEGER,'
            'guest_num INTEGER, price INTEGER)'

        )
        # id INTEGER PRIMARY KEY AUTOINCREMENT
        cursor.executescript(
            'CREATE TABLE IF NOT EXISTS `table_booking`'
            '(id_room INTEGER PRIMARY KEY,'
            'firstname TEXT, lastname TEXT, check_in TEXT, check_out TEXT'
            'FOREIGN KEY id_room REFERENCES `table_rooms` (id_room))'
        )


def get_all_rooms() -> list:
    with sqlite3.connect('table_hotels.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * from `table_rooms`')
        all_rooms = cursor.fetchall()

        room_request = []
        for row in all_rooms:
            room_request.append({"roomId": row[0],
                                 "floor": row[1],
                                 "guestNum": row[2],
                                 "beds": row[3],
                                 "price": row[4]})
        return room_request


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

        cursor.execute('SELECT a.id_room, a.floor, a.beds, a.guest_num, a.price '
                       'FROM `table_rooms` a, `table_booking` b '
                       'WHERE b.id_room = a.id_room AND b.check_in = ? AND b.check_out = ? '
                       'AND a.guest_num = ?', value)
        data = cursor.fetchall()

        room_request = []
        for row in data:
            room_request.append({"roomId": row[0],
                                 "floor": row[1],
                                 "guestNum": row[2],
                                 "beds": row[3],
                                 "price": row[4]})
        return room_request


def add_booking(value: tuple) -> None:
    with sqlite3.connect('table_hotels.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO `table_booking` '
            '(id_room, firstname, lastname, check_in, check_out) VALUES (?, ?, ?, ?, ?)',
            value
        )


def get_room_id(id: int) -> int:
    with sqlite3.connect('table_hotels.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) from `table_rooms`'
                       'WHERE id_room = ?', (id,))
        count_room = cursor.fetchone()[0]
        if count_room:
            return count_room
        return 0
