from sqlalchemy import Column, Integer, String, ForeignKey
from app.data._mysql.models import BaseModel
from sqlalchemy.orm import relationship


class Manufacturer(BaseModel["Manufacturer"]):
    __tablename__ = "manufacturers"

    manufacturer_id = Column(Integer, autoincrement=True, primary_key=True)
    company_name = Column(String(45), nullable=False)
    head_office_phone = Column(String(25), nullable=False)
    head_office_address = Column(String(100), nullable=False)
    contact_person_id = Column(Integer, ForeignKey('contact_persons.contact_person_id'))

    contact_person = relationship('ContactPerson', back_populates="manufacturer", uselist=False)
    products = relationship('ManufacturerHasProduct', back_populates='manufacturer')
