from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Instruction(Base):
    __tablename__ = "instructions"

    id = Column(Integer, primary_key=True, index=True)
    doctor = Column(String)
    patient = Column(String)
    text = Column(String)
    acknowledged = Column(Boolean, default=False)
