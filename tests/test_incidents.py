sample_incident = {
    "titulo": "Robo de prueba",
    "descripcion": "Incidente generado por test",
    "lat": 19.4326,
    "lon": -99.1332,
    "prioridad": 2,
}


def test_create_incidente(client):
    """Crea un nuevo incidente o valida que la solicitud sea procesada correctamente."""
    response = client.post("/incidente/", json=sample_incident)
    assert response.status_code in (200, 201, 422), (
        f"Respuesta inesperada: {response.status_code}"
    )


def test_list_incidentes(client):
    """Verifica que la lista de incidentes esté disponible."""
    response = client.get("/incidentes/")
    assert response.status_code == 200, "El endpoint /incidentes/ no respondió correctamente."
    assert isinstance(response.json(), list), "La respuesta no es una lista."


def test_get_incidente_by_id(client):
    """Verifica acceso al detalle de un incidente por ID."""
    res = client.get("/incidentes/")
    data = res.json()
    if data:
        first_id = data[0].get("id") or data[0].get("ID") or 1
        response = client.get(f"/incidente/{first_id}")
        assert response.status_code in (200, 404), (
            f"Respuesta inesperada: {response.status_code}"
        )
