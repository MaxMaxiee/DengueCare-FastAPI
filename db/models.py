from db.database import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from uuid import uuid4

class DbUser(Base):
    __tablename__ = 'users'
    age = Column(String)
    approved = Column(Boolean, default = False)
    contact_number = Column(String)
    email = Column(String)
    firstname = Column(String)
    id = Column(String, primary_key = True, default=lambda: str(uuid4()))
    is_pending = Column(Boolean, default = True)
    is_verified = Column(Boolean, default = False)
    lastname = Column(String)
    password = Column(String)
    purok = Column(String)
    role = Column(String)
    sex = Column(String)

