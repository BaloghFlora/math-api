# app/models.py

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class MathRequest(Base):
    __tablename__ = "math_requests"

    id = Column(Integer, primary_key=True, index=True)
    operation = Column(String, index=True)
    input_data = Column(String)
    result = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
