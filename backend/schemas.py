from pydantic import BaseModel

class InstructionCreate(BaseModel):
    doctor: str
    patient: str
    text: str

class InstructionOut(InstructionCreate):
    id: int
    acknowledged: bool

    class Config:
        orm_mode = True

