from fastapi import HTTPException
from models.groupa import Groupa
from models.student import Student


def create_student(form, db, current_user):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Faqat admin o‘quvchi qo‘sha oladi!")

    if form.groupa_id is not None:
        group = db.query(Groupa).filter(Groupa.id == form.groupa_id).first()
        if not group:
            raise HTTPException(status_code=404, detail="Bunday guruh topilmadi!")

    new_student = Student(
        full_name=form.full_name,
        groupa_id=form.groupa_id,
        is_archived=form.is_archived if form.is_archived is not None else False
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return {"message": "Yangi o‘quvchi qo‘shildi", "student_id": new_student.id}


def update_student(student_id: int, form, db, current_user):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Bunday ID li o‘quvchi topilmadi!")

    if current_user.role == "admin":
        if form.groupa_id is not None:
            group = db.query(Groupa).filter(Groupa.id == form.groupa_id).first()
            if not group:
                raise HTTPException(status_code=404, detail="Bunday guruh mavjud emas!")

        db.query(Student).filter(Student.id == student_id).update({
            Student.full_name: form.full_name,
            Student.groupa_id: form.groupa_id,
            Student.is_archived: form.is_archived
        })
        db.commit()
        return {"message": "O‘quvchi ma’lumotlari yangilandi!"}
    else:
        raise HTTPException(status_code=403, detail="Siz admin emassiz!")

def archive_student(student_id: int, db, current_user):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Faqat admin arxivlashi mumkin!")

    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Bunday ID li o‘quvchi topilmadi!")

    student.is_archived = True
    db.commit()
    return {"message": "O‘quvchi arxivlandi."}


def create_admin(form, db, current_user):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Faqat admin o‘quvchi qo‘sha oladi!")

    if form.group_id is not None:
        group = db.query(Groupa).filter(Groupa.id == form.groupa_id).first()
        if not group:
            raise HTTPException(status_code=404, detail="Bunday guruh topilmadi!")

    new_student = Student(
        full_name=form.full_name,
        groupa_id=form.groupa_id,
        is_archived=form.is_archived if form.is_archived is not None else False
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return {"message": "Yangi admin qo‘shildi", "student_id": new_student.id}


