from typing import Optional
from sqlmodel import SQLModel


class NoteCreate(SQLModel):
    title: str
    content: str
    tags: Optional[str] = None
    author: Optional[str] = None
