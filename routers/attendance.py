from fastapi import APIRouter,Depends
from db import database
from models.users import Users
from routers.login import get_current_active_user
from schema.attendance import CreateAttendance ,UpdateAttendance
from functions.attendance import create_attendance, update_attendace,delete_attendence
from models.attendance import Attendance
from sqlalchemy.orm import Session


attendance = APIRouter(tags=["Attendance"])


@attendance.options('/attendance')
def head_yaratish(db: Session = Depends(database)):
    return db.query(Attendance).all()


@attendance.get('/get_attendance')
def get_users(db: Session = Depends(database),
              current_user: Users = Depends(get_current_active_user)):

    if current_user.role == "admin":
        return db.query(Attendance).all()
    else:
        return db.query(Attendance).filter(Attendance.id == current_user.id).first()


@attendance.get('/atendance_view')
def attendence_get(db: Session = Depends(database)):
    return db.query(Attendance).all()


@attendance.post('/create_atendance')
def creates_attendance(form: CreateAttendance, db: Session = Depends(database)):
    return create_attendance(form,db)


@attendance.put('/update_atendance')
def update_attendance(ident: int, form: UpdateAttendance,db: Session = Depends(database),
                      current_user: Users = Depends(get_current_active_user)):
    return update_attendace(ident, form,db,current_user)


@attendance.delete('/delete_atendance')
def delete_attendance(ident: int, db: Session = Depends(database),
                      current_user: Users = Depends(get_current_active_user)):
    return delete_attendence(ident,db,current_user)

