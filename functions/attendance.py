from fastapi import HTTPException
from models.attendance import Attendance
from models.groupa import Groupa


def create_attendance(form,db):
    new = Attendance(
        user_id = form.user_id,
        student_id = form.student_id,
        date_time = form.date_time,
        status = form.status,
        groupa_id = form.groupa_id,
    )
    db.add(new)
    db.commit()
    return {"Message": "Davomat qushildi "}


def update_attendace(student_id: int, form, db, current_user):
    student = db.query(Attendance).filter(Attendance.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Bunday ID li o‘quvchi topilmadi!")

    if current_user.role == "admin":
        if form.groupa_id is not None:
            group = db.query(Groupa).filter(Groupa.id == form.groupa_id).first()
            if not group:
                raise HTTPException(status_code=404, detail="Bunday guruh mavjud emas!")

        db.query(Attendance).filter(Attendance.id == student_id).update({
            Attendance.student_id: form.student_id,
            Attendance.date_time: form.date_time,
            Attendance.groupa_id: form.groupa_id,
            Attendance.status : form.status,
            Attendance.user_id : form.user_id
        })
        db.commit()
        return {"message": "Attendance ma’lumotlari yangilandi!"}
    else:
        raise HTTPException(status_code=403, detail="Siz admin emassiz!")

def delete_attendence(ident, db, current_user):
    delete = db.query(Attendance).filter(Attendance.id == ident).first()
    if not delete:
        raise HTTPException(404,"Bunday id li mavjud emas ")
    if current_user.role != 'admin':
        db.query(Attendance).filter(Attendance.id == ident).delete()
        db.commit()
        return {"Message": "Attendence delete "}
    else:
        raise HTTPException(404,"Siz admin emasiz !! ")

