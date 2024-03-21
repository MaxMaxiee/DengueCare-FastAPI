from sqlalchemy.orm import Session
from schemas import UserBase
from db.models import DbUser
from db.hash import Hash
from fastapi import HTTPException, status


def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        age = request.age,
        contact_number = request.contact_number,
        email = request.email,
        firstname = request.firstname,
        lastname = request.lastname,
        purok = request.purok,
        password = Hash.bcrypt(request.password),
        role = request.role,
        sex = request.sex,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all_user(db: Session):
    return db.query(DbUser).all()

def get_user_by_id(db: Session, id: str):
    user = db.query(DbUser).filter(DbUser.id.contains(id)).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {id} not found')

def get_user_by_username(db: Session, username: str):
    user = db.query(DbUser).filter(DbUser.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with username {username} not found')
    return user

def update_user_by_id(db: Session, id:str, request:DbUser):
    user = db.query(DbUser).filter(DbUser.id.contains(id))
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {id} not found')
    user.update({
        DbUser.age: request.age,
        DbUser.contact_number: request.contact_number,
        DbUser.email: request.email,
        DbUser.firstname: request.firstname,
        DbUser.lastname: request.lastname,
        DbUser.purok: request.purok,
        DbUser.password: Hash.bcrypt(request.password),
        DbUser.role: request.role,
        DbUser.sex: request.sex,
    })
    db.commit()
    return user

def delete_user_by_id(db: Session, id: str):
    user = db.query(DbUser).filter(DbUser.id.contains(id)).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {id} not found')
    db.delete(user)
    db.commit()
    return {'message': f'User with id {id} has been deleted'}