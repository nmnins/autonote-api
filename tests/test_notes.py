from .conftest import auth_headers  # ou adapte l'import si nécessaire


def test_create_notes_authorized(client):
    response = client.post(
        "/notes",
        headers=client.auth_headers(),
        json={
            "title": "test 1",
            "content": "test de l'app",
            "tags": "test",
            "author": "moi",
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["content"] == "test de l'app"


def test_create_notes_with_invalid_key(client):
    response = client.post(
        "/notes",
        headers=client.auth_headers(valid=False),
        json={
            "title": "test 1",
            "content": "test de l'app",
            "tags": "test",
            "author": "moi",
        },
    )
    assert response.status_code == 403


def test_create_notes(client):
    response = client.post(
        "/notes",
        json={
            "title": "test 1",
            "content": "test de l'app",
            "tags": "test",
            "author": "moi",
        },
    )
    assert response.status_code == 403


def test_get_all_notes_authorized(client):
    client.post(
        "/notes",
        headers=auth_headers(),
        json={
            "title": "test 1",
            "content": "test de l'app",
            "tags": "test",
            "author": "moi",
        },
    )
    response = client.get("/notes", headers=auth_headers())
    assert response.status_code == 200
    notes = response.json()
    assert isinstance(notes, list)
    assert len(notes) == 1
    assert notes[0]["content"] == "test de l'app"


def test_get_all_notes_with_invalid_key(client):
    client.post(
        "/notes",
        headers=auth_headers(),
        json={
            "title": "test 1",
            "content": "test de l'app",
            "tags": "test",
            "author": "moi",
        },
    )
    response = client.get("/notes", headers=auth_headers(valid=False))
    assert response.status_code == 403


def test_get_all_notes(client):
    client.post(
        "/notes",
        headers=auth_headers(),
        json={
            "title": "test 1",
            "content": "test de l'app",
            "tags": "test",
            "author": "moi",
        },
    )
    response = client.get("/notes")
    assert response.status_code == 403


def test_get_note_authorized(client):
    create = client.post(
        "/notes",
        headers=auth_headers(),
        json={
            "title": "test 1",
            "content": "test de l'app",
            "tags": "test",
            "author": "moi",
        },
    )
    note_id = create.json()["id"]
    response = client.get(f"/notes/{note_id}", headers=auth_headers())
    assert response.status_code == 200
    assert response.json()["id"] == note_id


def test_get_note_with_invalid_key(client):
    create = client.post(
        "/notes",
        headers=auth_headers(),
        json={
            "title": "test 1",
            "content": "test de l'app",
            "tags": "test",
            "author": "moi",
        },
    )
    note_id = create.json()["id"]
    response = client.get(f"/notes/{note_id}", headers=auth_headers(valid=False))
    assert response.status_code == 403


def test_get_note(client):
    create = client.post(
        "/notes",
        headers=auth_headers(),
        json={
            "title": "test 1",
            "content": "test de l'app",
            "tags": "test",
            "author": "moi",
        },
    )
    note_id = create.json()["id"]
    response = client.get(f"/notes/{note_id}")
    assert response.status_code == 403


def test_delete_item_authorized(client):

    create = client.post(
        "/notes",
        headers=auth_headers(),
        json={
            "title": "test 1",
            "content": "test de l'app",
            "tags": "test",
            "author": "moi",
        },
    )
    note_id = create.json()["id"]

    response = client.delete(f"/notes/{note_id}", headers=auth_headers())
    assert response.status_code == 204

    # vérifier que l'id n’existe plus
    response = client.get(f"/notes/{note_id}", headers=auth_headers())
    assert response.status_code == 404


def test_delete_item_with_invalid_key(client):
    # Creer d'abord une note à supprimer
    create = client.post(
        "/notes",
        headers=auth_headers(),
        json={
            "title": "test 1",
            "content": "test de l'app",
            "tags": "test",
            "author": "moi",
        },
    )
    note_id = create.json()["id"]

    response = client.delete(f"/notes/{note_id}", headers=auth_headers(valid=False))
    assert response.status_code == 403


def test_delete_item(client):
    # Creer d'abord une note à supprimer
    create = client.post(
        "/notes",
        headers=auth_headers(),
        json={
            "title": "test 1",
            "content": "test de l'app",
            "tags": "test",
            "author": "moi",
        },
    )
    note_id = create.json()["id"]

    response = client.delete(f"/notes/{note_id}")
    assert response.status_code == 403
