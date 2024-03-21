from fastapi import APIRouter, Depends
from schemas import UserBase, UserDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user
from typing import List
from auth.oauth2 import get_current_user


router = APIRouter(
    prefix='/user',
    tags=['user'],
)

# Router for creating a user
@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)

# Router for getting all users
@router.get('/', response_model=List[UserDisplay])
def get_all_user(db:Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return db_user.get_all_user(db)

# Router for getting a specif user using ID
@router.get('/{id}', response_model=UserBase)
def get_user_by_id(id: str, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return db_user.get_user_by_id(db, id)

# Router for updating user info
@router.put('/{id}', response_model=UserBase)
def update_user_by_id(id: str, request: UserBase, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return db_user.update_user_by_id(db, id, request)

@router.delete('/{id}')
def delete_user_by_id(id: str, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return db_user.delete_user_by_id(db, id)







