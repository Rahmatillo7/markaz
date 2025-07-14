from sqlalchemy import Column, String, Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from db import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80), nullable=False)
    username = Column(String(80), nullable=False)
    password = Column(String(80), nullable=False)
    token = Column(String(80), nullable=True)
    address = Column(String(80), nullable=False)
    numer = Column(Integer, nullable=False)
    email = Column(String(80), nullable=False)
    role = Column(String(90), nullable=False)
    images = Column(String(90), nullable=True)
    groupa_id = Column(Integer, ForeignKey("groupa.id"), nullable=False)

    attendances = relationship("Attendance", back_populates="user")
    teacher_profile = relationship("Teacher", back_populates="user")



