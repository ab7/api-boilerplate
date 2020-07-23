from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import SessionLocal


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
async def root():
    return {'message': 'Hello, World!'}


@app.get('/users', response_model=List[schemas.User])
async def users_get(offset: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(models.User).offset(offset).limit(limit).all()
    return users


@app.post('/users', response_model=schemas.User)
def users_create(user: schemas.UserCreate, db: Session = Depends(get_db)):
    user = models.User(username=user.username, email=user.email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
