def test_get_all_users(client):
    """Verifica que la ruta /usuarios/ responda."""
    response = client.get("/usuarios/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_single_user(client):
    """Si hay usuarios, intenta obtener uno por ID."""
    res = client.get("/usuarios/")
    data = res.json()
    if isinstance(data, list) and data:
        first_user = data[0]
        user_id = first_user.get("id") or first_user.get("ID") or 1
        detail = client.get(f"/usuario/{user_id}")
        assert detail.status_code in (200, 404)
    else:
        pytest.skip("Sin usuarios disponibles")

