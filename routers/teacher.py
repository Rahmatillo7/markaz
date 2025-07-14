from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from db import database
from models.teacher import Teacher
from functions.teacher import teacher_qoshish,teacher_delete,teacher_update
from models.users import Users
from routers.login import get_current_user, get_current_active_user
from schema.teacher import CreateaTeacher,UpdateTeacher


router = APIRouter(tags=["Teacher"])


@router.get("/get_teacher")
def get_users(db: Session = Depends(database),
              current_user: Users = Depends(get_current_active_user)):

    if current_user.role == "admin":
        return db.query(Teacher).all()
    else:
        return db.query(Teacher).filter(Teacher.user_id == current_user.id).all()


@router.post('/create/teachers')
def teachers_qushish(form: CreateaTeacher, db: Session = Depends(database),
                    current_user: Users = Depends(get_current_user)):
    return teacher_qoshish(form, db,current_user)


@router.post('/teachers_admin')
def teachers_admin_qushish(form: CreateaTeacher, db: Session = Depends(database),
                    current_user: Users = Depends(get_current_user)):
    return teacher_qoshish(form, db,current_user)


@router.put('/teachers_edit/(teacher_id}')
def teachers_edit(ident: int, form: UpdateTeacher, db: Session = Depends(database),
                 current_user: Users = Depends(get_current_user)):
    return teacher_update(ident,form,db,current_user)


@router.delete('/teachers_vomiting/(teacher_id)')
def teachers_delete(ident: int, db: Session = Depends(database),
                   current_user: Users = Depends(get_current_user)):
    return teacher_delete(ident,db, current_user)