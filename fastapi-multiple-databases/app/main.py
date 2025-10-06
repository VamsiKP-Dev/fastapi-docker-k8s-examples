
# app/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import app.database as database
import app.schemas as schemas
import app.crud_db1 as crud_db1
import app.crud_db2 as crud_db2

app = FastAPI(title="Multi-DB Example")

# create tables at startup
@app.on_event("startup")
def on_startup():
    database.init_db()

# Dependency functions to get sessions for each DB
def get_db1():
    db = database.SessionLocalDB1()
    try:
        yield db
    finally:
        db.close()

def get_db2():
    db = database.SessionLocalDB2()
    try:
        yield db
    finally:
        db.close()

# ----- DB1 (Users) endpoints -----
@app.post("/users/", response_model=schemas.UserRead)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db1)):
    return crud_db1.create_user(db, user)

@app.get("/users/", response_model=List[schemas.UserRead])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db1)):
    return crud_db1.list_users(db, skip, limit)

@app.get("/users/{user_id}", response_model=schemas.UserRead)
def read_user(user_id: int, db: Session = Depends(get_db1)):
    u = crud_db1.get_user(db, user_id)
    if not u:
        raise HTTPException(status_code=404, detail="User not found")
    return u

# ----- DB2 (Notes) endpoints -----
@app.post("/notes/", response_model=schemas.NoteRead)
def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db2)):
    return crud_db2.create_note(db, note)

@app.get("/notes/", response_model=List[schemas.NoteRead])
def read_notes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db2)):
    return crud_db2.list_notes(db, skip, limit)

@app.get("/notes/user/{user_id}", response_model=List[schemas.NoteRead])
def read_notes_by_user(user_id: int, db: Session = Depends(get_db2)):
    return crud_db2.list_notes_by_user(db, user_id)

# Optional combined endpoint: fetch user from DB1 and notes from DB2
@app.get("/user-with-notes/{user_id}")
def user_with_notes(user_id: int, db1: Session = Depends(get_db1), db2: Session = Depends(get_db2)):
    user = crud_db1.get_user(db1, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    notes = crud_db2.list_notes_by_user(db2, user_id)
    return {"user": user, "notes": notes}
