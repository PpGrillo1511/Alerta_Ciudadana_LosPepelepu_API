import pytest
import mysql.connector


def test_generar_datos(client):
    """Debe generar datos de prueba correctamente."""
    response = client.post("/generar-datos/")
    assert response.status_code in (200, 201), (
        f"Error al generar datos: {response.status_code}"
    )


def test_generar_usuarios(client):
    """Debe generar usuarios de prueba correctamente."""
    response = client.post("/generar-usuarios/")
    assert response.status_code in (200, 201), (
        f"Error al generar usuarios: {response.status_code}"
    )


def test_generar_incidentes(client):
    """Debe generar incidentes correctamente."""
    response = client.post("/generar-incidentes/")
    assert response.status_code in (200, 201), (
        f"Error al generar incidentes: {response.status_code}"
    )


def test_generar_comentarios(client):
    """Debe generar comentarios correctamente."""
    response = client.post("/generar-comentarios/")
    assert response.status_code in (200, 201), (
        f"Error al generar comentarios: {response.status_code}"
    )


def test_incidentes_prioridad(client):
    """Prueba /incidentes_prioridad y la omite si no hay conexión MySQL."""
    try:
        response = client.get("/incidentes_prioridad")
        assert response.status_code == 200, (
            f"Respuesta inesperada: {response.status_code}"
        )
    except mysql.connector.errors.DatabaseError:
        pytest.skip("MySQL no disponible en entorno CI/CD.")
