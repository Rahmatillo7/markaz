from pydantic import BaseModel

class CreateGroupa(BaseModel):
    name : str
    user_id : int
    days : str
    teacher_id : int

class UpdateGroupa(BaseModel):
    name : str
    user_id : int
    days : str
    teacher_id : int

