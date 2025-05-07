import tempfile
import pytest
from sqlmodel import SQLModel, create_engine, Session
from fastapi.testclient import TestClient
from app.main import app
from app.models.note import Note

# Créer un fichier temporaire SQLite
def override_get_engine():
    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".db")
    engine = create_engine(f"sqlite:///{tmp_file.name}", connect_args={"check_same_thread": False})
    SQLModel.metadata.create_all(engine)
    return engine

# Override la DB de l'app pour les tests
engine = override_get_engine()

@app.on_event("startup")
def startup_override():
    app.state.db_engine = engine

@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c
