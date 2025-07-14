from models.users import Users
from sqladmin import ModelView

class UsersAdmin(ModelView, model = Users):

    column_list = [Users.id , Users.name, Users.username, Users.password, Users.numer, Users.address,Users.email,Users.role,Users.groupa_id]
    name_plural = 'Users'