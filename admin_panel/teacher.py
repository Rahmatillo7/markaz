from models.teacher import Teacher
from sqladmin import ModelView

class TeacherAdmin(ModelView, model= Teacher):
    column_list = [Teacher.id, Teacher.date_time, Teacher.subject, Teacher.salary, Teacher.user_id]
    name_plural = "Teacher"