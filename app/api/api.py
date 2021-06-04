from typing import List, Iterator

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session, sessionmaker

from api import models, schemas
from api.db import SessionLocal


app = FastAPI()


def get_db() -> Iterator[sessionmaker]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
async def root() -> dict:
    return {'message': 'Hello, World!'}


@app.get('/users', response_model=List[schemas.User])
async def users_get(offset: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> dict:
    users = db.query(models.User).offset(offset).limit(limit).all()
    return users


@app.post('/users', response_model=schemas.User)
def users_create(user: schemas.UserCreate, db: Session = Depends(get_db)) -> dict:
    user = models.User(username=user.username, email=user.email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
