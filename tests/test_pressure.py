
from fastapi.testclient import TestClient


def test_create_pressure_measurement(client: TestClient):
    # First, create a user
    client.post("/users/", json={"id": 2001, "telegram_nickname": "pressureuser"})

    response = client.post(
        "/pressure/",
        json={
            "telegram_nickname": "pressureuser",
            "measurements": [{"up": 120, "down": 80, "pulse": 60}],
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["up"] == 120
    assert data[0]["down"] == 80
    assert data[0]["pulse"] == 60
    assert "id" in data[0]
    assert "measurement_time" in data[0]


def test_create_pressure_measurement_for_nonexistent_user(client: TestClient):
    response = client.post(
        "/pressure/",
        json={
            "telegram_nickname": "nonexistentuser",
            "measurements": [{"up": 120, "down": 80, "pulse": 60}],
        },
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}


def test_create_multiple_pressure_measurements(client: TestClient):
    # First, create a user
    client.post("/users/", json={"id": 2002, "telegram_nickname": "pressureuser2"})

    response = client.post(
        "/pressure/",
        json={
            "telegram_nickname": "pressureuser2",
            "measurements": [
                {"up": 120, "down": 80, "pulse": 60},
                {"up": 130, "down": 90},
            ],
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["up"] == 120
    assert data[1]["up"] == 130

