from sqlmodel import SQLModel, Field


class NoteCreate(SQLModel):
    content: str = Field(..., min_length=5, max_length=100)
