from sqlalchemy import Column, Integer, String, Date, Enum, Text, DateTime, text
import enum

from app.core.database import Base


class Gender(str, enum.Enum):
    male = "male"
    female = "female"
    other = "other"


class Status(str, enum.Enum):
    active = "active"
    inactive = "inactive"


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
    status = Column(Enum(Status), nullable=False, server_default="active")
    is_deleted = Column(Integer, nullable=False, server_default="0")
    created_at = Column(
        DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP")
    )
