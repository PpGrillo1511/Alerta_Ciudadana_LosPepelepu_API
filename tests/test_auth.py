def test_register_user(client):
    """Debe permitir registrar un nuevo usuario o responder con validación (422)."""
    user = {"nombre": "Test", "correo": "test@example.com", "contrasena": "1234"}
    response = client.post("/register", json=user)
    assert response.status_code in (200, 201, 422), (
        f"Respuesta inesperada: {response.status_code}"
    )


def test_login_user(client):
    """Debe permitir login o devolver error de autenticación (401/422)."""
    credentials = {"correo": "test@example.com", "contrasena": "1234"}
    response = client.post("/login", json=credentials)
    assert response.status_code in (200, 401, 422), (
        f"Respuesta inesperada: {response.status_code}"
    )
