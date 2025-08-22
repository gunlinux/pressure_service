
from fastapi.testclient import TestClient


def test_create_user(client: TestClient):
    response = client.post("/users/", json={"id": 12345, "telegram_nickname": "testuser"})
    assert response.status_code == 200
    data = response.json()
    assert data["telegram_nickname"] == "testuser"
    assert data["id"] == 12345
    assert "registration_data" in data


def test_create_duplicate_user(client: TestClient):
    # Create a user first
    client.post("/users/", json={"id": 54321, "telegram_nickname": "duplicate_user"})
    
    # Try to create a user with the same nickname but different ID
    response = client.post("/users/", json={"id": 98765, "telegram_nickname": "duplicate_user"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Telegram nickname already registered"}

