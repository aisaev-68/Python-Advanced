from .app import db
from typing import Dict, Any


class Client(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    credit_card = db.Column(db.String(50))
    car_number = db.Column(db.String(10))

    def to_json(self) -> Dict[str, Any]:
        return {c.name: getattr(self, c.name) for c in
                self.__table__.columns}


class Parking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(100), nullable=False)
    opened = db.Column(db.Boolean, default=False) # индикатор открыта ли парковка
    count_places = db.Column(db.Integer, nullable=False) # общее количество мест на данной парковке
    count_available_places = db.Column(db.Integer, nullable=False) # количество свободных мест на данной парковке

    def to_json(self) -> Dict[str, Any]:
        return {c.name: getattr(self, c.name) for c in
                self.__table__.columns}


class ClientParking(db.Model):
    __tablename = 'client_parking'
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    parking_id = db.Column(db.Integer, db.ForeignKey('parking.id'))
    time_in = db.Column(db.DATETIME)
    time_out = db.Column(db.DATETIME)
    client = db.relationship('Client', backref='client_parking')
    parking = db.relationship('Parking', backref='client_parking')
    # __table_args__ = (db.UniqueConstraint(client_id, parking_id, name='unique_client_parking'),)

    def to_json(self) -> Dict[str, Any]:
        return {c.name: getattr(self, c.name) for c in
                self.__table__.columns}

