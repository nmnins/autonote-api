import tempfile
import json
import os
import pytest
from app.routes import notes
from pathlib import Path


# éxécuté automatiquement avant chaque test avec autouse=True
@pytest.fixture(autouse=True)
def fake_data_file():
    # créer un fichier temporaire JSON vide
    with tempfile.NamedTemporaryFile(delete=False, mode="w+", suffix=".json") as tmp:
        json.dump({}, tmp)
        tmp_path = tmp.name

    # Remplacer DATA_FILE par le fichier temporaire
    notes.DATA_FILE = Path(tmp_path)

    # Recharger les notes à partir de ce fichier
    notes.notes = notes.load_notes()
    notes.note_id_counter = max(notes.notes.keys(), default=0) + 1

    yield

    # Nettoyage après le test
    os.remove(tmp_path)
