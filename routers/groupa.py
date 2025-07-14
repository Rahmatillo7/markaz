from fastapi import APIRouter,Depends
from db import database
from sqlalchemy.orm import Session
from functions.groupa import guruh_delete,groupa_qushish,groupa_yaratish,groupa_yangilash
from models.users import Users
from routers.login import get_current_active_user
from schema.groupa import CreateGroupa,UpdateGroupa
from models.groupa import Groupa


routers_groupa = APIRouter(tags=["Groupa"])


@routers_groupa.get('/get_kurish')
def get_users(db: Session = Depends(database),
              current_user: Users = Depends(get_current_active_user)):

    if current_user.role == "admin":
        return db.query(Groupa).all()
    else:
        return db.query(Groupa).filter(Groupa.id == current_user.id).first()


@routers_groupa.post('/teacher_qushish_guruh')
def teacher_guruh_yaratish(form: CreateGroupa, db: Session = Depends(database),
                           current_user: Users = Depends(get_current_active_user)):
    return groupa_qushish(form,db,current_user)


@routers_groupa.post('/admin_guruh_yaratish')
def admin_guruh_qushish(form: CreateGroupa , db: Session = Depends(database),
                        current_user: Users = Depends(get_current_active_user)):
    return groupa_yaratish(form,db,current_user)


@routers_groupa.put('/admin_yangilash_guruh')
def admin_guruh_yaratish(ident:int ,form: UpdateGroupa, db: Session = Depends(database),
                         current_user: Users = Depends(get_current_active_user)):
    return groupa_yangilash(ident,form,db,current_user)


@routers_groupa.delete('/admin_guruh_uchirsh')
def guruh_uchirish(ident: int, db: Session = Depends(database),
                   current_user: Users = Depends(get_current_active_user)):
    return guruh_delete(ident,db,current_user)