from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.data._mysql.models import BaseModel
from app.data._mysql.models.associations.store_has_supplier import stores_has_suppliers


class Supplier(BaseModel):
    __tablename__ = "suppliers"

    supplier_id = Column(Integer, autoincrement=True, primary_key=True)
    company_name = Column(String(45), nullable=False)
    head_office_phone = Column(String(25), nullable=False)
    head_office_address = Column(String(100), nullable=False)

    contact_person_id = Column(Integer, ForeignKey("contact_persons.contact_person_id"), nullable=True)

    stores = relationship(
        "Store",
        secondary=stores_has_suppliers,
        back_populates="suppliers"
    )
