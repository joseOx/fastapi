from fastapi.testclient import TestClient
from app.main import app

# Creamos el cliente de pruebas
client = TestClient(app)

def test_read_main():
    """Prueba que el root funcione"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API funcionando con estructura de Routers"}

def test_create_task():
    """Prueba crear una tarea"""
    payload = {
        "title": "Aprender Testing",
        "description": "Usar Pytest con FastAPI"
    }
    response = client.post("/tasks/", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Aprender Testing"
    assert "id" in data # Verifica que la BD asignó un ID