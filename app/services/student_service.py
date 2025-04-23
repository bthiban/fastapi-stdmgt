from sqlalchemy import update

from app.models.student import Student
from app.schemas.student_schema import StudentCreate, StudentUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status


async def get_all_students(db: AsyncSession):
    result = await db.execute(select(Student))
    return result.scalars().all()


async def create_student(db: AsyncSession, student_in: StudentCreate):
    # check exist
    result = await db.execute(select(Student).where(Student.email == student_in.email))
    existing = result.scalars().first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Student with this email already exist.",
        )

    student = Student(**student_in.model_dump())
    db.add(student)
    await db.commit()
    await db.refresh(student)
    return student


async def update_student(db: AsyncSession, student_id: int, student_in: StudentUpdate):
    result = await db.execute(select(Student).where(Student.id == student_id))
    student = result.scalar_one_or_none()
    if not student:
        return None

    for key, value in student_in.model_dump(exclude_unset=True).items():
        setattr(student, key, value)

    await db.commit()
    await db.refresh(student)
    return student


async def delete_student(db: AsyncSession, student_id: int):
    result = await db.execute(select(Student).where(Student.id == student_id))
    student = result.scalar_one_or_none()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    await db.execute(
        update(Student).where(Student.id == student_id).values(is_deleted=1)
    )
    await db.commit()
