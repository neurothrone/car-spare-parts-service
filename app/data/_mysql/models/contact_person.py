from sqlalchemy import Column, Integer, String

from app.data._mysql.models import BaseModel


class ContactPerson(BaseModel):
    __tablename__ = "contact_persons"

    contact_person_id = Column(Integer, autoincrement=True, primary_key=True)
    first_name = Column(String(length=45), nullable=False)
    last_name = Column(String(length=45), nullable=False)
    phone = Column(String(length=25), nullable=False)
    email = Column(String(length=100), nullable=False)
