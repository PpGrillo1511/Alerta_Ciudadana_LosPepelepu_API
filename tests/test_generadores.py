def test_generar_datos(client):
    response = client.post("/generar-datos/")
    assert response.status_code in (200, 201)


def test_generar_usuarios(client):
    response = client.post("/generar-usuarios/")
    assert response.status_code in (200, 201)


def test_generar_incidentes(client):
    response = client.post("/generar-incidentes/")
    assert response.status_code in (200, 201)


def test_generar_comentarios(client):
    response = client.post("/generar-comentarios/")
    assert response.status_code in (200, 201)


def test_incidentes_prioridad(client):
    response = client.get("/incidentes_prioridad")
    assert response.status_code == 200
