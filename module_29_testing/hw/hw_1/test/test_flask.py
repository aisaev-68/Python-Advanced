import json
import pytest


def test_get_client_by_id(client) -> None:
    resp = client.get("clients/1")
    data = json.loads(resp.data.decode())
    assert data['name'] == 'name'


def test_clients(client) -> None:
    resp = client.get("/clients/1")
    assert resp.status_code == 200
    assert resp.json == {"id": 1, "name": "name", "surname": "surname",
                         "credit_card": "4444DA77777777", "car_number": "A555AA55"}


def test_create_client(client) -> None:
    client_data = {"name": "Никита", "surname": "Нестеренко",
                   "credit_card": "99999999999", "car_number": "B666BB66"}
    resp = client.post("/clients", data=json.dumps(client_data), headers={'Content-Type': 'application/json'})

    assert resp.status_code == 201


def test_create_parking(client) -> None:
    parking_data = {"address": "Москва, ул. Мясницкая, 23", "opened": True,
                    "count_places": 50, "count_available_places": 50}
    resp = client.post("/parkings", data=json.dumps(parking_data),
                       headers={'Content-Type': 'application/json'})

    assert resp.status_code == 201


@pytest.mark.parking
def test_in_parking(client):
    data = {"client_id": 1, "parking_id": 1}
    resp = client.post("/client_parkings", data=json.dumps(data),
                       headers={'Content-Type': 'application/json'})
    assert resp.status_code == 201


@pytest.mark.parking
def test_out_parking(client):
    data = {"client_id": 1, "parking_id": 1}
    resp = client.delete("/client_parkings", data=json.dumps(data),
                         headers={'Content-Type': 'application/json'})
    assert resp.status_code == 201


def test_app_config(app):
    assert not app.config['DEBUG']
    assert app.config['TESTING']
    assert app.config['SQLALCHEMY_DATABASE_URI'] == "sqlite://"


@pytest.mark.parametrize("route", ["/clients", "/clients/1", "/"])
def test_route_status(client, route):
    rv = client.get(route)
    assert rv.status_code == 200
