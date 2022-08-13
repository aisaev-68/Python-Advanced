from typing import List
import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify, render_template

db = SQLAlchemy()


def create_app():
    """
    Фабрика приложений
    """
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///prod.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["'SQLALCHEMY_ECHO'"] = True
    db.init_app(app)

    from .models import Client, Parking, ClientParking

    @app.before_request
    def before_request_func():
        db.create_all()

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.session.remove()

    @app.route("/clients", methods=['GET'])
    def get_clients():
        """
        Получение списка всех клиентов
        """
        clients: List[Client] = db.session.query(Client).all()
        clients_list = [c.to_json() for c in clients]
        return jsonify(clients_list), 200

    @app.route("/clients/<int:client_id>", methods=['GET'])
    def get_info_client_by_id(client_id: int):
        """
        Получение информации о клиенте по ID
        """
        client: Client = db.session.query(Client).get(client_id)
        return jsonify(client.to_json()), 200

    @app.route("/clients", methods=['POST'])
    def add_client():
        """
        Создание нового клиента
        """
        data = request.get_json()
        if data:
            db.session.add(Client(**data))
            db.session.commit()
            return 'Клиент добавлен', 201
        else:
            return 404

    @app.route("/parkings", methods=['POST'])
    def add_parking():
        """
        Создание новой парковочной зоны
        """
        data = request.json
        if data:
            db.session.add(Parking(**data))
            db.session.commit()
            return 'Новая парковочная зона добавлена', 201
        else:
            return 'Получены неправильные данные', 404

    @app.route("/client_parkings", methods=['POST', 'DELETE'])
    def in_client_park():
        """
        Заезд(Выезд) на парковку (проверить, открыта ли парковка, количество свободных мест
        на парковке уменьшается, фиксируется дата заезда, при выезде наоборот).
        В теле запроса передать client_id, parking_id.
        """
        data = request.get_json()

        if data:
            parking_id = data['parking_id']
            client_id = data['client_id']
            parking: Parking = db.session.query(Parking).get(parking_id)

            if request.method == 'POST':
                if parking.opened and parking.count_available_places > 0:
                    parking.count_available_places = parking.count_available_places - 1
                    db.session.add(ClientParking(client_id=client_id, parking_id=parking_id,
                                                 time_in=datetime.datetime.now()))
                    db.session.commit()
                    return 'Клиент припарковал авто', 201
                else:
                    return 'Парковка не работает или нет мест', 202

            elif request.method == 'DELETE':
                client_parking: ClientParking = db.session.query(ClientParking)\
                    .filter(ClientParking.client_id == client_id, ClientParking.time_out == None).one_or_none()
                if client_parking:
                    parking.count_available_places = parking.count_available_places + 1
                    client_parking.time_out = datetime.datetime.now()
                    db.session.commit()
                    return 'Клиент покинул парковку', 201
                else:
                    return 'Клиент не парковал авто на парковке', 201

        else:
            return 'Получены неправильные данные', 404

    @app.route("/", methods=['GET'])
    def get_template_handler() -> str:
        """Получение UI-интерфейса все актуальныз припаркованных авто"""

        in_client_parking = db.session.query(ClientParking).filter(ClientParking.time_out == None).all()
        # print(in_client_parking)
        packaging_by_clients = []
        for p in in_client_parking:
            # print(p.to_json()) # {'id': 2, 'client_id': 2, 'parking_id': 1, 'time_in': datetime.datetime(2022, 8, 13, 14, 5, 21, 518197), 'time_out': None}
            # print(11, p.client.to_json()) #{'id': 2, 'name': 'Bob', 'surname': 'Smit', 'credit_card': '122221111111A23', 'car_number': 'A111AA99'}
            # print(22, p.parking.to_json())
            parking_obj = dict(**p.to_json(),
                               client=p.client.to_json(),
                               parking=p.parking.to_json())
            packaging_by_clients.append(parking_obj)
        return render_template("in_clients_parking.html",
                               parkings=packaging_by_clients)

    return app
