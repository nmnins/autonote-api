from sqlmodel import SQLModel, Field
from typing import Optional

class Note(SQLModel, table=True): 
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str = Field(..., min_length=5, max_length=100)