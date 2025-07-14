from pydantic import BaseModel, EmailStr


class CreateUsers(BaseModel):
    name: str
    username: str
    password: str
    address: str
    numer: int
    email: EmailStr
    groupa_id : int


class UpdateUsers(BaseModel):
    name: str
    username: str
    password: str
    address: str
    numer: int
    email: EmailStr
    groupa_id : int