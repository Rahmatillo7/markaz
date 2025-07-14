from typing import Optional
from pydantic import BaseModel

class CreateStudent(BaseModel):
    full_name: str
    groupa_id: Optional[int] = None
    is_archived: str


class UpdateStudent(BaseModel):
    full_name: Optional[str] = None
    groupa_id: Optional[int] = None
    is_archived: str
