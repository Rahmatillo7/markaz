from models.groupa import Groupa
from sqladmin import ModelView

class GroupaAdmin(ModelView, model=Groupa):
    column_list = [Groupa.id, Groupa.user_id, Groupa.days, Groupa.name]
    name_plural = "Groupa"