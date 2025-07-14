from datetime import date

from pydantic import BaseModel

class CreateAttendance(BaseModel):
    user_id : int
    date_time : date
    student_id : int
    status : str
    groupa_id : int


class UpdateAttendance(BaseModel):
    user_id: int
    student_id : int
    date_time: date
    status: str
    groupa_id : int