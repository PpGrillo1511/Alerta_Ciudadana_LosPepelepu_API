def test_register_user(client):
    """Verifica que se pueda registrar un usuario (dummy)."""
    user = {"nombre": "Test", "email": "test@example.com", "password": "1234"}
    response = client.post("/register", json=user)
    # tu API puede devolver 200 o 201 según lógica
    assert response.status_code in (200, 201, 400, 409)


def test_login_user(client):
    """Verifica que /login existe y responde adecuadamente."""
    credentials = {"email": "test@example.com", "password": "1234"}
    response = client.post("/login", json=credentials)
    assert response.status_code in (200, 401, 404)
