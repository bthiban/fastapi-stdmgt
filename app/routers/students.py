from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.services.student_service import (
    get_all_students,
    create_student,
    update_student,
    delete_student,
)
from app.schemas.student_schema import (
    StudentOut,
    StudentCreate,
    StudentUpdate
)
from typing import List

router = APIRouter(prefix="/students", tags=["students"])


@router.get("/", response_model=List[StudentOut])
async def list_students(db: AsyncSession = Depends(get_db)):
    return await get_all_students(db)


@router.post("/", response_model=StudentOut, status_code=201)
async def create_student_endpoint(
    student: StudentCreate, db: AsyncSession = Depends(get_db)
):
    return await create_student(db, student)


@router.put("/{student_id}", response_model=StudentUpdate)
async def update_student_endpoint(
    student_id: int, student: StudentUpdate, db: AsyncSession = Depends(get_db)
):
    updated = await update_student(db, student_id, student)
    if not updated:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated


@router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_student_endpoint(student_id: int, db: AsyncSession = Depends(get_db)):
    await delete_student(db, student_id)
