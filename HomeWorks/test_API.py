from tabnanny import check
import requests
import pytest

BASE_URL = "https://api.restful-api.dev/objects"

@pytest.fixture()
def obj_id():
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    # 1) получаем Response, 2) проверяем статус, 3) читаем json
    create_response  = requests.post(BASE_URL, json=payload, timeout=10)
    create_response.raise_for_status()
    oid = create_response.json()["id"]

    # отдаём id тесту
    yield oid

    # аккуратный teardown — двойное удаление не роняет фикстуру
    try:
        requests.delete(f"{BASE_URL}/{oid}", timeout=10)
    except Exception:
        pass

def test_create_object(obj_id):
    # Используем фикстуру, чтобы не мусорить
    # И в конце теста явно удаляем созданный объект
    payload = {
       "name": "Apple MacBook Pro 16",
       "data": {
          "year": 2018,
          "price": 1749.99,
          "CPU model": "Intel Core i9",
          "Hard disk size": "1 TB"
       }
    }
    response = requests.post(BASE_URL, json=payload).json()
    assert response['name'] == payload['name']
    # сразу подчистим, чтобы не засорять (этот объект создан без фикстуры)
    requests.delete(f"{BASE_URL}/{response['id']}")

def test_get_object(obj_id):
    print(obj_id)
    response = requests.get(f'{BASE_URL}?id=3&id=5&id={obj_id}').json()
    # проверяем, что в списке есть созданный объект
    ids = [obj['id'] for obj in response]
    assert obj_id in ids

def test_put_object(obj_id):
    payload = {
       "name": "Apple MacBook Pro 16",
       "data": {
          "year": 2025,
          "price": 2500.99,
          "CPU model": "M3",
          "Hard disk size": "1 TB"
       }
    }
    response = requests.put(f'{BASE_URL}/{obj_id}', json=payload).json()
    assert response['name'] == payload['name']

def test_delete_object(obj_id):
    # удаляем в тесте
    response = requests.delete(f'{BASE_URL}/{obj_id}')
    assert response.status_code == 200
    # проверяем, что не существует
    response = requests.get(f'{BASE_URL}/{obj_id}')
    assert response.status_code == 404
    # teardown тоже попытается удалить, но без падения (см. try/except)

