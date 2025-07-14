from models.users import Users
from routers.login import get_password_hash, get_current_user
from fastapi import HTTPException, Depends


def get_current_user_role(current_user: Users = Depends(get_current_user)):
    if current_user.role not in ["admin", "teacher"]:
        raise HTTPException(status_code=403, detail="Ruxsat yo'q")
    return current_user


def create_users(form,db,current_user):
    if current_user.role =='admin':

        new = Users(
            name=form.name,
            username=form.username,
            password=get_password_hash(form.password),
            address=form.address,
            numer=form.numer,
            email=form.email,
            groupa_id=form.groupa_id,
            role ='users'

        )
        db.add(new)
        db.commit()
        return {"Message": "Users qushildi !!! "}
    else:
        raise HTTPException(404,"Siz admin emasiz")



def create_teacher_vomiting(form,db,current_user):
    if current_user.role =='admin':
        new = Users(
            name=form.name,
            username=form.username,
            password=get_password_hash(form.password),
            address=form.address,
            numer=form.numer,
            email=form.email,
            groupa_id=form.groupa_id,
            role='teacher'
        )
        db.add(new)
        db.commit()
        return {"Message": "Teacher qushildi !!! "}
    else:
        raise HTTPException(404, "Siz admin emasiz !! ")


def create_admin_vomiting(form,db,current_user):
    if current_user.role =='admin':
        new = Users(
            name=form.name,
            username=form.username,
            password=get_password_hash(form.password),
            address=form.address,
            numer=form.numer,
            email=form.email,
            groupa_id = form.groupa_id,
            role='admin'
        )
        db.add(new)
        db.commit()
        return {"Message": "Admin qushildi !!! "}
    else:
        raise HTTPException(404, "Siz admin emasiz !! ")


def users_update_teacher(ident,form,db,current_user):
    a = db.query(Users).filter(Users.id == ident).first()
    if not a:
        raise HTTPException(404,"Siz qidirgan id li mavjud emas !!! ")

    if current_user.role =='admin':

        db.query(Users).filter(Users.id == ident).update({
            Users.name : form.name,
            Users.username : form.username,
            Users.password : form.password,
            Users.address : form.address,
            Users.numer : form.numer,
            Users.email : form.email,
            Users.groupa_id : form.groupa_id,
        })
        db.commit()
        return {"Message": "Users yangilandi !!! "}
    else:
        raise HTTPException(404,"Siz admin emasz !!! ")



def teacher_admin_edit(ident,form,db,current_user):
    a = db.query(Users).filter(Users.id == ident).first()
    if not a:
        raise HTTPException(404,"Siz qidirgan id li mavjud emas !!! ")

    if current_user.role =='admin':

        db.query(Users).filter(Users.id == ident).update({
            Users.name : form.name,
            Users.username : form.username,
            Users.password : form.password,
            Users.address : form.address,
            Users.numer : form.numer,
            Users.email : form.email,
            Users.groupa_id : form.groupa_id,
        })
        db.commit()
        return {"Message": "teacher Yangilandi !!! "}
    else:
        raise HTTPException(404,"Siz admin emasz !!! ")


def users_delete(ident,db,current_user):
    delete = db.query(Users).filter(Users.id == ident).first()
    if not delete:
        raise HTTPException(404,"Siz qidirgan id li mavjud emas !!! ")

    if current_user.role == 'admin':
        db.query(Users).filter(Users.id == ident).delete()
        db.commit()
        return {"Message": "Users uchirildi"}
    else:
        raise HTTPException(404,"Siz admin emasz !!! ")


def delete_admin_teacher(ident,db,current_user):
    delete = db.query(Users).filter(Users.id == ident).first()
    if not delete:
        raise HTTPException(404,"Siz qidirgan id li mavjud emas !!! ")

    if current_user.role == 'admin':
        db.query(Users).filter(Users.id == ident).delete()
        db.commit()
        return {"Message": "teacher uchirildi"}
    else:
        raise HTTPException(404,"Siz admin emasz !!! ")
