from sqlalchemy import Column, Integer, String, Date, Enum, Text, DateTime
from sqlalchemy.sql import func
import enum

from app.core.database import Base


# pylint: disable=too-few-public-methods
class Gender(str, enum.Enum):
    male = "male"
    female = "female"
    other = "other"


# pylint: disable=too-few-public-methods
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    dob = Column(Date, nullable=False)
    gender = Column(Enum(Gender))
    address = Column(Text)
    email = Column(String(100))
    phone = Column(String(20))
    enrollment_year = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now)
