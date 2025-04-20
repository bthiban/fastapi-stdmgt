from pydantic import BaseModel, EmailStr
from datetime import datetime, date
from typing import Optional
from enum import Enum


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


class StudentUpdate(StudentCreate):
    pass


class StudentOut(StudentCreate):
    id: int
    created_at: datetime

    model_config = {"from_attributes": True}
