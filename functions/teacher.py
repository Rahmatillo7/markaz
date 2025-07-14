from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.teacher import Teacher


def teacher_qoshish(form, db: Session, current_user):
    if current_user.role != "teacher":
        raise HTTPException(status_code=403, detail="Sizga ruxsat yo‘q")

    existing_teacher = db.query(Teacher).filter(Teacher.user_id == current_user.id).first()

    if existing_teacher:
        raise HTTPException(status_code=400, detail="Siz allaqachon teacher sifatida mavjudsiz")

    new_teacher = Teacher(
        subject=form.subject,
        user_id=current_user.id,
        date_time=form.date_time,
        salary=form.salary
    )
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    return {"message": "O‘qituvchi muvaffaqiyatli qo‘shildi"}


def teacher_update(teacher_id: int, form, db: Session, current_user):
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()

    if not teacher:
        raise HTTPException(status_code=404, detail="O‘qituvchi topilmadi")

    if teacher.user_id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Sizga ruxsat yo‘q")

    teacher.subject = form.subject
    teacher.date_time = form.date_time
    teacher.salary = form.salary
    db.commit()
    db.refresh(teacher)
    return {"message": "O‘qituvchi ma'lumotlari yangilandi"}


def teacher_delete(teacher_id: int, db: Session, current_user):
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()

    if not teacher:
        raise HTTPException(status_code=404, detail="O‘qituvchi topilmadi")

    if current_user.role != "admin" and teacher.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Sizga ruxsat yo‘q")

    db.delete(teacher)
    db.commit()

    return {"message": "O‘qituvchi muvaffaqiyatli o‘chirildi"}



def teacher_admin_qushish(form, db: Session, current_user):
    if current_user.role != "teacher":
        raise HTTPException(status_code=403, detail="Sizga ruxsat yo‘q")

    existing_teacher = db.query(Teacher).filter(Teacher.user_id == current_user.id).first()

    if existing_teacher:
        raise HTTPException(status_code=400, detail="Siz allaqachon teacher sifatida mavjudsiz")

    new_teacher = Teacher(
        subject=form.subject,
        user_id=current_user.id,
        date_time=form.date_time,
        salary=form.salary
    )
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    return {"message": "Admin teacher muvaffaqiyatli qo‘shildi"}

