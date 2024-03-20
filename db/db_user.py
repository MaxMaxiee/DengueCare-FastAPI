from sqlalchemy.orm import Session
from schemas import UserBase
from db.models import DbUser

def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        age = request.age,
        approved = request.approved,
        contact_number = request.contact_number,
        email = request.email,
        firstname = request.firstname,
        is_pending = request.is_verified,
        lastname = request.lastname,
        purok = request.purok,
        role = request.role,
        sex = request.sex,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user