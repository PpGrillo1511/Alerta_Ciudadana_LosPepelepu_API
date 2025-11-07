def test_root(client):
    """Verifica que la raíz devuelva el mensaje de bienvenida."""
    response = client.get("/")
    assert response.status_code == 200, (
        f"Respuesta inesperada: {response.status_code}"
    )
    data = response.json()
    assert isinstance(data, list), "La respuesta no es una lista."
    assert any("Bienvenido" in str(item) for item in data), (
        f"El mensaje esperado no se encontró en la respuesta: {data}"
    )


def test_docs_available(client):
    """Confirma que la documentación interactiva (Swagger UI) esté accesible."""
    response = client.get("/docs")
    assert response.status_code == 200, "La ruta /docs no está disponible."


def test_openapi_schema(client):
    """Verifica que el esquema OpenAPI esté disponible."""
    response = client.get("/openapi.json")
    assert response.status_code == 200, "No se pudo obtener el esquema OpenAPI."
    data = response.json()
    assert "info" in data, "La respuesta no contiene el campo 'info'."
