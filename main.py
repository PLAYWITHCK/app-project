from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="EduShare Hub API")

notes_db = [
    {"id": 1, "title": "Calculus I Derivatives Cheat Sheet", "subject": "Mathematics", "price": "2.99", "is_free": False},
    {"id": 2, "title": "Organic Chemistry Reaction Map", "subject": "Chemistry", "price": "FREE", "is_free": True},
    {"id": 3, "title": "World History Timeline", "subject": "History", "price": "1.49", "is_free": False},
]


class NoteUpload(BaseModel):
    id: int
    title: str
    subject: str
    price: str
    is_free: bool


@app.get("/api/notes")
def get_notes():
    return notes_db


@app.post("/api/upload")
def upload_note(note: NoteUpload):
    note_data = note.model_dump()
    if note_data["is_free"]:
        note_data["price"] = "FREE"
    notes_db.append(note_data)
    return {"message": "Note uploaded successfully", "note": note_data}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
