from models.attendance import Attendance
from sqladmin import ModelView

class AttendanceAdmin(ModelView, model= Attendance):
    column_list = [Attendance.id , Attendance.user_id, Attendance.status, Attendance.date_time, Attendance.groupa_id]
    name_plural = "Attendance"