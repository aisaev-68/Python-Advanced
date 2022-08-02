from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_all_recipes():
    response = client.get("/books/")
    if response.status_code == 200:
        print('Тест эдпойнт /books/ завершен успешно')
    else:
        print('Тест эдпойнт /books/ завершен с ошибкой')
    # assert response.json() == {"msg": "Hello World"}


def test_get_recipes_by_id(recipes_id: int):
    response = client.get(f"/books/{recipes_id}")
    if response.status_code == 200:
        print('Тест эдпойнт /books/{recipes_id} завершен успешно')
    else:
        print('Тест эдпойнт /books/{recipes_id} завершен с ошибкой')
    # assert response.json() == {"msg": "Hello World"}


if __name__ == "__main__":
    test_get_all_recipes()
    test_get_recipes_by_id(1)
