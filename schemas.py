from pydantic import BaseModel

class UserBase(BaseModel):
    age = str
    approved = bool
    contact_number = str
    email = str
    firstname = str
    id = int
    is_pending = bool
    is_verified = bool
    lastname = str
    purok = str
    role = str
    sex = str

class UserDisplay(BaseModel):
    age = str
    approved = bool
    contact_number = str
    email = str
    firstname = str
    is_pending = bool
    is_verified = bool
    lastname = str
    purok = str
    role = str
    sex = str
    class Config():
        from_attributes = True
