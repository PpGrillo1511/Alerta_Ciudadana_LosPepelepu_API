from main import app
from fastapi.testclient import TestClient

import pytest

@pytest.fixture(scope="module")
def client():
    """Cliente de pruebas para la API."""
    with TestClient(app) as c:
        yield c
