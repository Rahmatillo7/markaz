from datetime import datetime

from pydantic import BaseModel

class CreateaTeacher(BaseModel):
    subject :str
    user_id : int
    date_time :datetime
    salary : int

class UpdateTeacher(BaseModel):
    subject: str
    user_id: int
    date_time: datetime
    salary: int