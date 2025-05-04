from pydantic import BaseModel, Field

class NoteCreate(BaseModel):
    content: str = Field(..., min_length=5, max_length=100)
