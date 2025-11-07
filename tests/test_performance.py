import time

def test_api_response_time(client):
    """Verifica que la API responde en menos de 400 ms (según estándar del proyecto)."""
    start = time.perf_counter()
    response = client.get("/")
    elapsed = (time.perf_counter() - start) * 1000
    assert response.status_code == 200
    assert elapsed <= 400, f"La respuesta fue muy lenta: {elapsed:.2f} ms"
