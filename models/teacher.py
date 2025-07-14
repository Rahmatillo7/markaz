from sqlalchemy import Column, String, Integer, ForeignKey,DateTime
from sqlalchemy.orm import relationship

from db import Base

class Teacher(Base):
    __tablename__ = 'teacher'
    id = Column(Integer, primary_key=True,autoincrement=True)
    subject = Column(String(90),nullable=False)
    user_id = Column(Integer,ForeignKey('users.id'),nullable=False)
    date_time = Column(DateTime,nullable=False)
    salary = Column(Integer,nullable=False)

    user = relationship("Users", back_populates="teacher_profile")
    groups = relationship("Groupa", back_populates="teacher")

