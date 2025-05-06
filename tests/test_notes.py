from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_notes():
    response = client.post("/notes", json={"content": "Bonjour"})
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["content"] == "Bonjour"


def test_get_all_notes():
    client.post("/notes", json={"content": "Hello"})
    response = client.get("/notes")
    assert response.status_code == 200
    notes = response.json()
    assert isinstance(notes, list)
    assert len(notes) == 1
    assert notes[0]["content"] == "Hello"


def test_get_note():
    # créer d'abord une note à tester
    create = client.post("/notes", json={"content": "Test Notes"})
    note_id = create.json()["id"]

    response = client.get(f"/notes/{note_id}")
    assert response.status_code == 200
    assert response.json()["id"] == note_id


def test_delete_item():
    # Creer d'abord une note à supprimer
    create = client.post("/notes", json={"content": "Note à supp"})
    note_id = create.json()["id"]

    response = client.delete(f"/notes/{note_id}")
    assert response.status_code == 204

    # vérifier que l'id n’existe plus
    response = client.get(f"/notes/{note_id}")
    assert response.status_code == 404
