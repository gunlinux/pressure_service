
from fastapi.testclient import TestClient


def test_create_user(client: TestClient):
    response = client.post("/users/", json={"telegram_nickname": "testuser"})
    assert response.status_code == 200
    data = response.json()
    assert data["telegram_nickname"] == "testuser"
    assert "id" in data
    assert "registration_data" in data


def test_create_duplicate_user(client: TestClient):
    response = client.post("/users/", json={"telegram_nickname": "testuser"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Telegram nickname already registered"}

