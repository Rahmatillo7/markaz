from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(60), nullable=False)
    is_archived = Column(Boolean, default=False)
    groupa_id = Column(Integer, ForeignKey("groupa.id"), nullable=True)

    group = relationship("Groupa", back_populates="students")
    attendance = relationship("Attendance", back_populates="student")
