from sqlalchemy.orm import Session
from schemas import UserBase
from db.models import DbUser
from db.hash import Hash


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