from pydantic import BaseModel
from typing import Dict, Any, List

class Screen(BaseModel):
    id: int
    name: str
    branch_id: int
    class Config: orm_mode = True

class SignageContent(BaseModel):
    id: int
    name: str
    content_data: Dict[str, Any]
    class Config: orm_mode = True

class Playlist(BaseModel):
    id: int
    name: str
    schedule: Dict[str, Any]
    content: List[SignageContent] = []
    class Config: orm_mode = True
