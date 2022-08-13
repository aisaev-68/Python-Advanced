import datetime

import pytest
from flask import template_rendered
from ..app.app import create_app, db as _db
from ..app.models import Client, Parking, ClientParking


@pytest.fixture
def app():
    _app = create_app()
    _app.config["TESTING"] = True
    _app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"

    with _app.app_context():
        _db.create_all()
        client = Client(id=1,
                        name="name",
                        surname="surname",
                        credit_card='4444DA77777777',
                        car_number='A555AA55')
        parking = Parking(address="Moscow, str. 1",
                          opened=True,
                          count_places=90,
                          count_available_places=90)
        # in_client_parking = ClientParking(client_id=1,
        #                                   parking_id=1,
        #                                   time_in=datetime.datetime.now())
        # parking.count_available_places = parking.count_available_places - 1
        _db.session.add(client)
        _db.session.add(parking)
        # _db.session.add(in_client_parking)
        _db.session.commit()

        yield _app
        _db.session.close()
        _db.drop_all()


@pytest.fixture
def client(app):
    client = app.test_client()
    yield client


@pytest.fixture
def captured_templates(app):
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)


@pytest.fixture
def db(app):
    with app.app_context():
        yield _db
