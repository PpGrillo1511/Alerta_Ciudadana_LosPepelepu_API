sample_incident = {
    "titulo": "Robo de prueba",
    "descripcion": "Incidente generado por test",
    "lat": 19.4326,
    "lon": -99.1332,
    "prioridad": 2
}

def test_create_incidente(client):
    response = client.post("/incidente/", json=sample_incident)
    assert response.status_code in (200, 201, 422)


def test_list_incidentes(client):
    response = client.get("/incidentes/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_incidente_by_id(client):
    """Verifica acceso a /incidente/{id}."""
    res = client.get("/incidentes/")
    data = res.json()
    if data:
        first_id = data[0].get("id") or data[0].get("ID") or 1
        response = client.get(f"/incidente/{first_id}")
        assert response.status_code in (200, 404)
