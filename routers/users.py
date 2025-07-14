from fastapi import APIRouter, Depends, HTTPException
from fastapi import UploadFile
from sqlalchemy.orm import Session
from db import database
from functions.users import teacher_admin_edit, users_delete, create_teacher_vomiting,create_admin_vomiting, users_update_teacher, delete_admin_teacher,create_users
from models.users import Users
from routers.login import get_current_active_user
from schema.users import CreateUsers, UpdateUsers
from utlis.save_file import save_file


routers_users = APIRouter(tags=["Users"])


@routers_users.get("/view_users")
def get_view(db: Session = Depends(database),
              current_user: Users = Depends(get_current_active_user)):

    if current_user.role == "admin":
        return db.query(Users).all()
    else:
        return db.query(Users).filter(Users.id == current_user.id).first()


@routers_users.post('/create_user')
def create_user(form: CreateUsers, db: Session = Depends(database),
                current_user: Users = Depends(get_current_active_user)):
    return create_users(form,db,current_user)


@routers_users.post('/teacher_create')
def create_teachers(form: CreateUsers, db: Session = Depends(database),
                  current_user: Users = Depends(get_current_active_user)):
    return create_teacher_vomiting(form, db, current_user)


@routers_users.post('/admin_create')
def create_teacher(form: CreateUsers, db: Session = Depends(database),
                    current_user: Users = Depends(get_current_active_user)):
    return create_admin_vomiting(form,db,current_user)


@routers_users.put('/users_update')
def update_users(ident: int, form: UpdateUsers, db: Session = Depends(database),
                  current_user: Users = Depends(get_current_active_user)):
    return users_update_teacher(ident, form, db, current_user)


@routers_users.put('/admin_update')
def admin_users_update(ident: int, form: UpdateUsers, db: Session = Depends(database),
                    current_user: Users = Depends(get_current_active_user)):
    return teacher_admin_edit(ident, form, db, current_user)


@routers_users.delete('/user_delete')
def delete_users(ident: int, db: Session = Depends(database),
               current_user: Users = Depends(get_current_active_user)):
    return users_delete(ident, db, current_user)


@routers_users.delete('/admin_delete')
def delete_admin(ident: int, db: Session = Depends(database),
                  current_user: Users = Depends(get_current_active_user)):
    return delete_admin_teacher(ident, db, current_user)


@routers_users.put('/image')
def rasm_qushish(ident: int, file: UploadFile, db: Session = Depends(database),
                 current_user: Users = Depends(get_current_active_user)):
    user = db.query(Users).filter(Users.id == ident).first()
    if not user:
        raise HTTPException(404, "Siz qidirgan foydalanuvchi topilmadi")
    user.images = save_file(file)
    db.commit()
    return {"message": "Rasm qo‘shildi!"}


@routers_users.get("/protected")
def protected_route(current_user: Users =Depends(get_current_active_user)):
    return {"message": f"Xush kelibsiz, {current_user.username}. Sizning rolingiz: {current_user.role}"}


