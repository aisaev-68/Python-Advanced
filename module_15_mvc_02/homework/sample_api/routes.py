from flask import Flask, request, jsonify
from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField
from wtforms.validators import InputRequired
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

    if request.args.get('checkIn') and request.args.get('checkIn') != '':
        check_in = request.args.get('checkIn', type=str)

    if request.args.get('checkOut') and request.args.get('checkOut') != '':
        check_out = request.args.get('checkOut', type=str)

    if request.args.get('guestsNum') and request.args.get('guestsNum') != 0:
        guests_num = request.args.get('guestsNum', type=int)

    val = (check_in, check_out, guests_num)
    room_request = get_room_booking(val)

    schema["rooms"] = room_request
    return jsonify(schema)


@app.route('/booking', methods=['POST'])
def new_booking():
    room_id = None
    check_in = None
    check_out = None
    firstname = None
    lastname = None
    room_request = []
    request_booking = request.get_json()
    if request_booking:

        if 'bookingDates' in request_booking:
            check_in = request_booking['bookingDates']['checkIn']
            check_out = request_booking['bookingDates']['checkOut']

        if 'firstName' in request_booking:
            firstname = request_booking['firstName']

        if 'lastName' in request_booking:
            lastname = request_booking['lastName']

        if 'roomId' in request_booking:
            room_id = request_booking['roomId']
        if get_room_id(room_id):
            add_booking((room_id, firstname, lastname, check_in, check_out))
    else:
        room_request = get_all_rooms()

    schema["rooms"] = room_request
    return jsonify(schema)


if __name__ == '__main__':
    init_db()
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
