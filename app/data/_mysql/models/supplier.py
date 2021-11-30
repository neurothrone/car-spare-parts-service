from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.data._mysql.models import Base


class Supplier(Base):
    __tablename__ = "suppliers"

    supplier_id = Column(Integer, autoincrement=True, primary_key=True)
    company_name = Column(String(45), nullable=False)
    head_office_phone = Column(String(25), nullable=False)
    head_office_address = Column(String(100), nullable=False)
    contact_person_id = Column(Integer, ForeignKey("contact_persons.contact_person_id"), nullable=True)

    contact_person = relationship("ContactPerson", back_populates="supplier")
    products = relationship("ProductHasSupplier", back_populates="supplier")
    stores = relationship("StoreHasSupplier", back_populates="supplier")
