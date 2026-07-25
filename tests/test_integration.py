import os
import time
import requests
import pytest

BASE_URL = os.getenv('TEST_API_URL', 'http://localhost:5000')

def test_healthcheck():
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_crear_y_listar_noticia():
    # 1. Crear una noticia
    payload = {"titulo": "Integración con Docker Compose exitosa"}
    res_post = requests.post(f"{BASE_URL}/noticias", json=payload)
    assert res_post.status_code == 201
    assert res_post.json()["titulo"] == payload["titulo"]

    # 2. Consultar la lista y verificar que persiste en Postgres
    res_get = requests.get(f"{BASE_URL}/noticias")
    assert res_get.status_code == 200
    noticias = res_get.json()
    assert len(noticias) > 0
    assert any(n["titulo"] == payload["titulo"] for n in noticias)