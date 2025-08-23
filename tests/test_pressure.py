from fastapi.testclient import TestClient


def test_create_pressure_measurement(client: TestClient):
    # First, create a user
    user_id = 3001
    client.post('/users/', json={'id': user_id, 'telegram_nickname': 'pressureuser'})

    response = client.post(
        f'/users/{user_id}/pressure/',
        json=[{'up': 120, 'down': 80, 'pulse': 60}],
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]['up'] == 120
    assert data[0]['down'] == 80
    assert data[0]['pulse'] == 60
    assert 'id' in data[0]
    assert 'measurement_time' in data[0]


def test_create_pressure_measurement_for_nonexistent_user(client: TestClient):
    non_existent_user_id = 9999
    response = client.post(
        f'/users/{non_existent_user_id}/pressure/',
        json=[{'up': 120, 'down': 80, 'pulse': 60}],
    )
    assert response.status_code == 404
    assert response.json() == {'detail': 'User not found'}


def test_create_multiple_pressure_measurements(client: TestClient):
    # First, create a user
    user_id = 3002
    client.post('/users/', json={'id': user_id, 'telegram_nickname': 'pressureuser2'})

    response = client.post(
        f'/users/{user_id}/pressure/',
        json=[
            {'up': 120, 'down': 80, 'pulse': 60},
            {'up': 130, 'down': 90},
        ],
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]['up'] == 120
    assert data[1]['up'] == 130
