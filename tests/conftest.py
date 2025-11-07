import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture(scope="module")
def client():
    """Cliente de pruebas compartido para toda la suite."""
    with TestClient(app) as c:
        yield c
