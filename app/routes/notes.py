from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlmodel import Session, select
from app.models.note import Note
from app.models.noteCreate import NoteCreate
from fastapi import status
from app.core.auth import verify_api_key


notes_router = APIRouter(prefix="/notes", dependencies=[Depends(verify_api_key)])


@notes_router.post("/", status_code=201, response_model=Note)
def create_notes(note: NoteCreate, request: Request):
    engine = request.app.state.db_engine
    with Session(engine) as session:
        new_note = Note(
            title=note.title,
            content=note.content,
            tags=note.tags,
            author=note.author,
            created_at=datetime.now(timezone.utc),
        )
        session.add(new_note)
        session.commit()
        session.refresh(new_note)
    return new_note


@notes_router.get("/", response_model=list[Note])
def get_all_notes(request: Request):
    engine = request.app.state.db_engine
    with Session(engine) as session:
        result = session.exec(select(Note)).all()
    return result


@notes_router.get("/{id}", response_model=Note)
def get_note(id: int, request: Request):
    engine = request.app.state.db_engine
    with Session(engine) as session:
        note = session.get(Note, id)
        if not note:
            raise HTTPException(status_code=404, detail="Note non trouvée")
    return note


@notes_router.put("/{id}", response_model=Note)
def update_note(id: int, update_note: NoteCreate, request: Request):
    engine = request.app.state.db_engine
    with Session(engine) as session:
        note = session.get(Note, id)
        if not note:
            raise HTTPException(status_code=404, detail="Note non trouvée")
        note.title = update_note.title
        note.content = update_note.content
        note.tags = update_note.tags
        note.author = update_note.author
        note.updated_at = datetime.now(timezone.utc)
        session.commit()
        session.refresh(note)
    return note


@notes_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(id: int, request: Request):
    engine = request.app.state.db_engine
    with Session(engine) as session:
        note = session.get(Note, id)
        if not note:
            raise HTTPException(status_code=404, detail="Note non trouvée")
        session.delete(note)
        session.commit()
