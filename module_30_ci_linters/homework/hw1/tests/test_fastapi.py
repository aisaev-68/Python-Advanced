from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_get_all_recipes():
    response = client.get("/books/")
    assert response.status_code == 200


def test_get_recipes_by_id():
    response = client.get("/books/1")
    assert response.status_code == 200
