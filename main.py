from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
import models
from models import SessionLocal, engine

app = FastAPI()

# Pydantic Model
class UserCreate(BaseModel):
    name: str
    description: str

class UserUpdate(BaseModel):
    name: str = None
    description: str = None

# Dependency for create session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# New user
@app.post("/users/", response_model=UserCreate)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(name=user.name, description=user.description)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# List all users
@app.get("/users/")
async def read_users(limit: int = 10, db: Session = Depends(get_db)):
    # Default limit 10 users
    users = db.query(models.User).limit(limit).all()
    return users

# Update user
@app.put("/users/{user_id}")
async def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.name:
        db_user.name = user.name
    if user.description:
        db_user.description = user.description

    db.commit()
    db.refresh(db_user)
    return db_user

# Delete user
@app.delete("/users/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}
