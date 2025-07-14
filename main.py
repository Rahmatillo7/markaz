from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from admin_panel.login import AdminAuth
from routers.login import login_router, SECRET_KEY
from routers.users import routers_users
from admin_panel.users import UsersAdmin
from admin_panel.attendance import AttendanceAdmin
from db import engine
from routers.attendance import attendance
from routers.groupa import routers_groupa
from sqladmin import Admin
from routers.student import router_student
from routers.teacher import router
from admin_panel.groupa import GroupaAdmin
from admin_panel.teacher import TeacherAdmin
from admin_panel.student import StudentAdmin


app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key = SECRET_KEY)

app.include_router(routers_groupa)
app.include_router(login_router)
app.include_router(routers_users)
app.include_router(router_student)
app.include_router(attendance)




authentication_backend = AdminAuth(secret_key=SECRET_KEY)
admin = Admin(app,engine,authentication_backend=authentication_backend)

admin.add_model_view(UsersAdmin)
app.include_router(router)
admin.add_model_view(AttendanceAdmin)
admin.add_model_view(StudentAdmin)
admin.add_model_view(TeacherAdmin)
admin.add_model_view(GroupaAdmin)

