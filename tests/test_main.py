def test_root(client):
    """Verifica que la raíz devuelve el mensaje esperado."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    # Tu API devuelve una lista con un mensaje
    assert isinstance(data, list)
    assert any("Bienvenido" in str(item) for item in data)


def test_docs_available(client):
    response = client.get("/docs")
    assert response.status_code == 200


def test_openapi_schema(client):
    response = client.get("/openapi.json")
    assert response.status_code == 200
    data = response.json()
    assert "info" in data
