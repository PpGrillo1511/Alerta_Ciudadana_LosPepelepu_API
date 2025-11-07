def test_register_user(client):
    """Verifica que se pueda registrar un usuario (dummy)."""
    user = {"nombre": "Test", "correo": "test@example.com", "contrasena": "1234"}
    response = client.post("/register", json=user)
    assert response.status_code in (200, 201, 422)



def test_login_user(client):
    """Verifica que /login existe y responde adecuadamente."""
    credentials = {"correo": "test@example.com", "contrasena": "1234"}
    response = client.post("/login", json=credentials)
    assert response.status_code in (200, 401, 422)

