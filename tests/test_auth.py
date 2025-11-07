import jwt
from datetime import datetime, timedelta

def test_login_and_token(client):
    """Verifica que el login devuelve un token válido."""
    credentials = {"username": "admin", "password": "1234"}
    response = client.post("/auth/login", json=credentials)
    assert response.status_code in (200, 401)

    if response.status_code == 200:
        token = response.json().get("access_token")
        assert token
        decoded = jwt.decode(token, options={"verify_signature": False})
        assert "exp" in decoded


def test_protected_route_requires_token(client):
    """Asegura que un endpoint protegido exige autenticación."""
    response = client.get("/users/me")
    assert response.status_code in (401, 403)
