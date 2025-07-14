from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Attendance(Base):

    __tablename__ = "attendance"

    id = Column(Integer,primary_key=True, autoincrement=True)
    groupa_id = Column(Integer,ForeignKey("groupa.id"),nullable=False)
    student_id = Column(Integer, ForeignKey("students.id"))
    user_id = Column(Integer,ForeignKey("users.id"),nullable=False)
    date_time = Column(Date,nullable=False)
    status = Column(String(90),nullable=False)


    group = relationship("Groupa", back_populates="attendances")
    user = relationship("Users", back_populates="attendances")
    student = relationship("Student", back_populates="attendance")
