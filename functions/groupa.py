from fastapi import HTTPException
from models.groupa import Groupa


def groupa_qushish(form,db,current_user):
    if current_user !='teacher':
        new = Groupa(
            name = form.name,
            user_id = form.user_id,
            days = form.days,
            teacher_id = form.teacher_id
        )
        db.add(new)
        db.commit()
        return {"Message": "Groupa ochildi !!! "}
    else:
        raise HTTPException(404, "Siz teacher emasiz !!! ")


def groupa_yaratish(form,db,current_user):
    if current_user != 'admin':
        teacher = Groupa(
            name = form.name,
            user_id=form.user_id,
            days=form.days,
            teacher_id = form.teacher_id
        )
        db.add(teacher)
        db.commit()
        return {"Message": "Groupa qoshildi !!"}
    else:
        raise HTTPException(404,"Siz admin emasiz !! ")


def groupa_yangilash(ident,form,db,current_user):
    a = db.query(Groupa).filter(Groupa.id == ident).first()
    if not a:
        raise HTTPException(404,"Bunday idli mavjud emas !!! ")

    if not form.user_id or form.user_id == 0:
        raise HTTPException(400, " 0 chi id li bulishi mumkin emas !!")

    if current_user.role =='admin':
        db.query(Groupa).filter(Groupa.id == ident).update({
            Groupa.name : form.name,
            Groupa.user_id : form.user_id,
            Groupa.days : form.days,
            Groupa.teacher_id : form.teacher_id
        })
        db.commit()
        return {"Message": "groupa yangilandi !!! "}
    else:
        raise HTTPException(404, "Siz admin emasiz !!! ")


def guruh_delete(ident,db,current_user):
    delete = db.query(Groupa).filter(Groupa.id == ident).first()
    if not delete:
        raise HTTPException(404,"Bunday id li mavjud emas")
    if current_user.role=='admin':
        db.query(Groupa).filter(Groupa.id == ident).delete()
        db.commit()
        return {"Message": "Groupa uchirildi !!! "}
    else:
        raise HTTPException(404,"Siz admin emasiz !!! ")

