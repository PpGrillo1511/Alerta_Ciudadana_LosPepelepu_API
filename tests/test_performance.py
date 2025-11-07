import time


def test_api_response_time(client):
    """Verifica que la API responda en menos de 400 ms."""
    start = time.perf_counter()
    response = client.get("/")
    elapsed = (time.perf_counter() - start) * 1000
    assert response.status_code == 200, "La API no respondió correctamente."
    assert elapsed <= 400, f"Respuesta lenta: {elapsed:.2f} ms."
