from pydantic import BaseModel, EmailStr
from datetime import datetime, date
from typing import Optional
from enum import Enum

from app.models.student import Status


class Gender(str, Enum):
    male = "male"
    female = "female"
    other = "other"


class StudentCreate(BaseModel):
    full_name: str
    dob: date
    gender: Optional[Gender]
    address: Optional[str]
    email: Optional[EmailStr]
    phone: Optional[str]
    enrollment_year: Optional[int]


class StudentUpdate(BaseModel):
    full_name: Optional[str] = None
    dob: Optional[date] = None
    gender: Optional[Gender] = None
    address: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    enrollment_year: Optional[int] = None


class StudentOut(StudentCreate):
    id: int
    created_at: datetime
    status: Status
    is_deleted: int

    model_config = {"from_attributes": True}
