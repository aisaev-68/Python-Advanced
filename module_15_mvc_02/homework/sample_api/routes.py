from flask import Flask, request, jsonify
from models import init_db, add_room_db, add_booking, \
    get_all_rooms, get_room_booking, get_room_id
from schema import schema

app = Flask(__name__)


@app.route('/add-room', methods=['POST'])
def add_room():
    data = request.data
    floor = None
    beds = None
    guest_num = None
    price = None
    room_request = []
    if data:
        request_data = request.get_json()

        if 'floor' in request_data:
            floor = request_data['floor']

        if 'beds' in request_data:
            beds = request_data['beds']

        if 'guestNum' in request_data:
            guest_num = request_data['guestNum']

        if 'price' in request_data:
            price = request_data['price']

        add_room_db((floor, beds, guest_num, price))
    else:
        room_request = get_all_rooms()

    schema["rooms"] = room_request
    return schema


@app.route('/room', methods=['GET'])
def get_room():
    check_in = None
    check_out = None
    guests_num = 0
    result_data = {
        "rooms": []
    }

    if request.args.get('checkIn') and request.args.get('checkIn') != '':
        check_in = request.args.get('checkIn', type=str)

    if request.args.get('checkOut') and request.args.get('checkOut') != '':
        check_out = request.args.get('checkOut', type=str)

    if request.args.get('checkOut') and request.args.get('checkOut') != '':
        guests_num = request.args.get('guestsNum', type=int)

    busy_rooms = get_room_booking((guests_num, check_in, check_out))
    for item in get_all_rooms():
        if item[0] not in busy_rooms:
            room_request = {"roomId": item[0],
                            "floor": item[1],
                            "guestNum": item[2],
                            "beds": item[3],
                            "price": item[4]}

            result_data["rooms"].append(room_request)
    return jsonify(result_data)


@app.route('/booking', methods=['POST'])
def new_booking():
    room_id = None
    check_in = None
    check_out = None
    firstname = None
    lastname = None
    data = request.data
    if data:
        request_booking = request.get_json()
        if 'bookingDates' in request_booking:
            check_in = request_booking['bookingDates']['checkIn']
            check_out = request_booking['bookingDates']['checkOut']

        if 'firstName' in request_booking:
            firstname = request_booking['firstName']

        if 'lastName' in request_booking:
            lastname = request_booking['lastName']

        if 'roomId' in request_booking:
            room_id = request_booking['roomId']
        free_id_rooms = get_room_id()
        if room_id in free_id_rooms:
            add_booking((room_id, firstname, lastname, check_in, check_out))
            return 'The room succsessfully booked', 200
        else:
            return "Can't book same room twice", 409


if __name__ == '__main__':
    init_db()
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
