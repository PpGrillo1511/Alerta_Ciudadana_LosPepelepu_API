def test_root(client):
    """Verifica que la API responde correctamente en la raíz."""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json() or "status" in response.json()


def test_docs_available(client):
    """Verifica que la documentación Swagger está activa."""
    response = client.get("/docs")
    assert response.status_code == 200


def test_openapi_schema(client):
    """Verifica que el esquema OpenAPI se genera correctamente."""
    response = client.get("/openapi.json")
    assert response.status_code == 200
    data = response.json()
    assert "info" in data and "title" in data["info"]
