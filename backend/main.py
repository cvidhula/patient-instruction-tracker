from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import models, schemas
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/instructions")
def create_instruction(data: schemas.InstructionCreate):
    db = SessionLocal()
    inst = models.Instruction(**data.dict())
    db.add(inst)
    db.commit()
    db.refresh(inst)
    return inst

@app.get("/instructions")
def list_instructions():
    db = SessionLocal()
    return db.query(models.Instruction).all()

@app.post("/instructions/{id}/ack")
def acknowledge(id: int):
    db = SessionLocal()
    inst = db.query(models.Instruction).get(id)
    inst.acknowledged = True
    db.commit()
    return {"status": "acknowledged"}

