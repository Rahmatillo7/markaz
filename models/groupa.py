from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from db import Base

class Groupa(Base):

    __tablename__ = "groupa"

    id = Column(Integer,primary_key=True, autoincrement=True)
    name = Column(String(90),nullable=False)
    user_id = Column(Integer,ForeignKey("users.id"),nullable=False)
    days = Column(String(50),nullable=False)
    teacher_id = Column(Integer, ForeignKey("teacher.id"), nullable=True)

    attendances = relationship("Attendance", back_populates="group")
    students = relationship("Student", back_populates="group")

    teacher = relationship("Teacher", back_populates="groups")

