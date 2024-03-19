from db.database import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean

class DbUser(Base):
    __tablename__ = 'users'
    age = Column(String)
    approved = Column(Boolean)
    contact_number = Column(String)
    email = Column(String)
    firstname = Column(String)
    id = Column(Integer, primary_key=True, index=True)
    is_pending = Column(Boolean)
    is_verified = Column(Boolean)
    lastname = Column(String)
    purok = Column(String)
    role = Column(String)
    sex = Column(String)

