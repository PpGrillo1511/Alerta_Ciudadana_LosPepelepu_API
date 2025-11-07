import pytest
from fastapi.testclient import TestClient
from main import app  # tu main.py está en la raíz

@pytest.fixture(scope="module")
def client():
    """Cliente de pruebas para la API."""
    with TestClient(app) as c:
        yield c
