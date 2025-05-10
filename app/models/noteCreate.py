from datetime import datetime, timezone
from typing import Optional
from sqlmodel import SQLModel, Field


class NoteCreate(SQLModel):
    title: str
    content: str
    tags: Optional[str] = None  
    author: Optional[str] = None 


