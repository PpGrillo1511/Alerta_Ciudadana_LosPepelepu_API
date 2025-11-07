from fastapi.testclient import TestClient

sample_incident = {
    "type": "Robo",
    "description": "Prueba automatizada de incidente",
    "latitude": 19.4326,
    "longitude": -99.1332
}

def test_create_incident(client: TestClient):
    response = client.post("/incidents/", json=sample_incident)
    assert response.status_code in (200, 201)
    data = response.json()
    assert "id" in data or "message" in data


def test_list_incidents(client: TestClient):
    response = client.get("/incidents/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_incident_by_id(client: TestClient):
    """Si hay incidentes creados, obtiene el primero."""
    res = client.get("/incidents/")
    if res.json():
        first_id = res.json()[0].get("id")
        if first_id:
            detail = client.get(f"/incidents/{first_id}")
            assert detail.status_code == 200
