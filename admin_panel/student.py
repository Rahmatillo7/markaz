from models.student import Student
from sqladmin import ModelView

class StudentAdmin(ModelView, model = Student):
    column_list = [Student.id, Student.full_name, Student.is_archived, Student.groupa_id]
    name_plural = "Student"