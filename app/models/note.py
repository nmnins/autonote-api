from pydantic import BaseModel, Field


class Note(BaseModel):
    id: int
    content: str = Field(..., max_length=100)

 