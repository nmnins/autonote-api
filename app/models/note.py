from sqlmodel import SQLModel, Field
from datetime import datetime, timezone
from typing import Optional

class Note(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    content: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: Optional[datetime] = None
    tags: Optional[str] = None  
    author: Optional[str] = None 
