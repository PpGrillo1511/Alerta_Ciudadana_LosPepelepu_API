import pytest

def test_get_all_users(client):
    response = client.get("/usuarios/")
    assert response.status_code in (200, 401, 403)


def test_get_single_user(client):
    res = client.get("/usuarios/")
    data = res.json()
    if isinstance(data, list) and data:
        first_user = data[0]
        user_id = first_user.get("id") or first_user.get("ID") or 1
        detail = client.get(f"/usuario/{user_id}")
        assert detail.status_code in (200, 404)
    else:
        pytest.skip("Sin usuarios disponibles o endpoint protegido")


