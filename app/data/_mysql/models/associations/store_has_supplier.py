from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.data._mysql.models import BaseModel


class StoreHasSupplier(BaseModel):
    __tablename__ = "stores_has_suppliers"

    store_id = Column(Integer, ForeignKey("stores.store_id"), primary_key=True)
    supplier_id = Column(Integer, ForeignKey("suppliers.supplier_id"), primary_key=True)

    store = relationship("Store", back_populates="suppliers")
    supplier = relationship("Supplier", back_populates="stores")
