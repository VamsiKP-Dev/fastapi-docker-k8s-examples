
from sqlalchemy.orm import Session
import app.models as models
import app.schemas as schemas

def create_note(db: Session, note: schemas.NoteCreate) -> models.Note:
    db_note = models.Note(title=note.title, content=note.content)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def get_notes(db: Session):
    return db.query(models.Note).all()
