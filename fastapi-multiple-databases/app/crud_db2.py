
# app/crud_db2.py
from sqlalchemy.orm import Session
import app.models_db2 as models
import app.schemas as schemas

def create_note(db: Session, note: schemas.NoteCreate) -> models.Note:
    db_note = models.Note(user_id=note.user_id, title=note.title, content=note.content)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def list_notes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Note).offset(skip).limit(limit).all()

def list_notes_by_user(db: Session, user_id: int):
    return db.query(models.Note).filter(models.Note.user_id == user_id).all()
