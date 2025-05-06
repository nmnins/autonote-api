from fastapi import APIRouter, HTTPException
from app.models.note import Note
from app.models.noteCreate import NoteCreate
import json
from pathlib import Path


notes_router = APIRouter()

# Chemin vers le fichier JSON
DATA_FILE = Path(__file__).parent.parent / "notes.json"


# Charger les notes depuis le fichier
def load_notes():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
            return {int(k): Note(**v) for k, v in raw_data.items()}
    return {}


# Sauvegarder les notes dans le fichier
def save_notes():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump({k: v.model_dump() for k, v in notes.items()}, f, indent=2)


notes = load_notes()
note_id_counter = max(notes.keys(), default=0) + 1


@notes_router.post("/notes/", status_code=201)
def create_notes(note: NoteCreate):
    # récupérer la variable déclarée en dehors de la fonction
    global note_id_counter
    # créer une note avec un id unique
    new_note = Note(id=note_id_counter, content=note.content)
    # la stocker dans le dictionnaire
    notes[note_id_counter] = new_note
    # incrémenter le compteur
    note_id_counter += 1
    # retourner la note créée
    save_notes()
    return new_note


@notes_router.get("/notes/")
def get_all_notes():
    return list(notes.values())


@notes_router.get("/notes/{id}")
def get_note(id: int):
    if id not in notes:
        raise HTTPException(status_code=404, detail="Note not found")
    return notes[id]


@notes_router.put("/notes/{id}")
def update_note(id: int, update_note: NoteCreate):
    # vérifier si l'id est présent sinon retourner une erreur
    if id not in notes:
        raise HTTPException(status_code=404, detail="Note not found")
    # on remplace l'objet note par une nouvelle instance de Note
    updated_note = Note(id=id, content=update_note.content)
    notes[id] = updated_note
    save_notes()
    return updated_note


@notes_router.delete("/notes/{id}", status_code=204)
def delete_note(id: int):
    if id not in notes:
        raise HTTPException(status_code=404, detail="Note not found")
    del notes[id]
    save_notes()
    return {"message": f"Note {id} deleted successfully"}
