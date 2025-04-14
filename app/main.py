from sqlalchemy import text
from fastapi import FastAPI, Depends
from app.core.database import get_db
from sqlalchemy.orm import Session

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome!"}

@app.get("/ping-db")
def ping_db(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {"message": "DB connected!"}
