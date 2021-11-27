from sqlalchemy import Column, Integer, String, ForeignKey

from app.data._mysql.models import BaseModel


class Supplier(BaseModel):
    __tablename__ = "suppliers"

    supplier_id = Column(Integer, autoincrement=True, primary_key=True)
    company_name = Column(String(length=45), nullable=False)
    head_office_phone = Column(String(length=25), nullable=False)
    head_office_address = Column(String(length=100), nullable=False)

    contact_person_id = Column(Integer, ForeignKey("contact_persons.contact_person_id"), nullable=True)
