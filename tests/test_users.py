from fastapi.testclient import TestClient
from unittest.mock import patch
from sqlalchemy.exc import IntegrityError


def test_create_user(client: TestClient):
    response = client.post(
        '/users/', json={'id': 12345, 'telegram_nickname': 'testuser'}
    )
    assert response.status_code == 200
    data = response.json()
    assert data['telegram_nickname'] == 'testuser'
    assert data['id'] == 12345
    assert 'registration_data' in data


def test_create_duplicate_user(client: TestClient):
    # Create a user first
    client.post('/users/', json={'id': 54321, 'telegram_nickname': 'duplicate_user'})

    # Try to create a user with the same nickname but different ID
    response = client.post(
        '/users/', json={'id': 98765, 'telegram_nickname': 'duplicate_user'}
    )
    assert response.status_code == 400
    assert response.json() == {'detail': 'Telegram nickname already registered'}


def test_create_user_integrity_error(client: TestClient):
    with patch('app.api.endpoints.users.user_service.get_user_by_telegram_nickname', return_value=None):
        with patch('app.api.endpoints.users.user_service.create_user', side_effect=IntegrityError(None, None, None)):
            response = client.post(
                '/users/', json={'id': 111, 'telegram_nickname': 'integrity_error_user'}
            )
            assert response.status_code == 400
            assert response.json() == {'detail': 'Telegram nickname already registered'}
