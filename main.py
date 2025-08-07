# main.py

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app.operations import power, fibonacci, factorial
from app.database import SessionLocal, init_db
from app.models import MathRequest
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
init_db()

# Dependency: Get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Math API"}

@app.get("/power")
def compute_power(a: int, b: int, db: Session = Depends(get_db)):
    result = power(a, b)
    log = MathRequest(operation="power", input_data=f"{a},{b}", result=str(result))
    db.add(log)
    db.commit()
    return {"operation": "power", "a": a, "b": b, "result": result}

@app.get("/fibonacci")
def compute_fibonacci(n: int, db: Session = Depends(get_db)):
    try:
        result = fibonacci(n)
        log = MathRequest(operation="fibonacci", input_data=str(n), result=str(result))
        db.add(log)
        db.commit()
        return {"operation": "fibonacci", "n": n, "result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/factorial")
def compute_factorial(n: int, db: Session = Depends(get_db)):
    try:
        result = factorial(n)
        log = MathRequest(operation="factorial", input_data=str(n), result=str(result))
        db.add(log)
        db.commit()
        return {"operation": "factorial", "n": n, "result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
