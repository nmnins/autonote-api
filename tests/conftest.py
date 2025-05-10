import os

os.environ["API_KEY"] = "testApiKey123"
import tempfile
import pytest
from sqlmodel import SQLModel, create_engine
from fastapi import FastAPI
from fastapi.testclient import TestClient
from contextlib import asynccontextmanager

from app.routes.notes import notes_router


# Headers pour les tests
def auth_headers(valid=True):
    return {"x-api-key": os.environ["API_KEY"] if valid else "wrongkey"}


# Connexion db pour les tests
def get_test_engine():
    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".db")
    engine = create_engine(
        f"sqlite:///{tmp_file.name}", connect_args={"check_same_thread": False}
    )
    SQLModel.metadata.create_all(engine)
    return engine


# instance de fast api pr les tests
@pytest.fixture
def client():
    engine = get_test_engine()

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        app.state.db_engine = engine
        yield

    app = FastAPI(lifespan=lifespan)
    app.include_router(notes_router)

    with TestClient(app) as test_client:
        test_client.auth_headers = auth_headers
        yield test_client
