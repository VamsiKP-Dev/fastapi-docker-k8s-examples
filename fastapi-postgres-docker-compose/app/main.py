
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import app.schemas as schemas
import app.crud as crud
import app.database as database

app = FastAPI(title="Notes App with DB Container")

@app.on_event("startup")
def startup():
    database.init_db()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/notes/", response_model=schemas.NoteRead)
def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    return crud.create_note(db, note)

@app.get("/notes/", response_model=List[schemas.NoteRead])
def list_notes(db: Session = Depends(get_db)):
    return crud.get_notes(db)
