from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from functions.student import create_student,update_student,archive_student
from db import database
from models.users import Users
from models.student import Student
from routers.login import get_current_active_user
from schema.student import CreateStudent,UpdateStudent

router_student = APIRouter(tags=["Student"])


@router_student.get("/get_student")
def get_users(db: Session = Depends(database),
              current_user: Users = Depends(get_current_active_user)):

    if current_user.role == "admin":
        return db.query(Student).all()
    else:
        return db.query(Student).filter(Student.id == current_user.id).first()


@router_student.get("/create_get")
def get_arxiv_kurish(db: Session = Depends(database),
              current_user: Users = Depends(get_current_active_user)):

    if current_user.role == "admin":
        return db.query(Users).all()
    else:
        return db.query(Users).filter(Users.id == current_user.id).first()


@router_student.post("/create_users")
def student_create(form: CreateStudent, db: Session = Depends(database),
                   current_user: Users = Depends(get_current_active_user)):
    return create_student(form,db,current_user)


@router_student.post("/create_admin")
def student_create(form: CreateStudent, db: Session = Depends(database),
                   current_user: Users = Depends(get_current_active_user)):
    return create_student(form,db,current_user)


@router_student.put("/student_edit")
def student_update(form: UpdateStudent, db: Session = Depends(database),
                   current_user: Users = Depends(get_current_active_user)):
    return update_student(form,db,current_user)


@router_student.patch("/archive/{student_id}")
def student_archive(student_id : int, db: Session = Depends(database),
                    current_user: Users = Depends(get_current_active_user)):
    return archive_student(student_id,db,current_user)
