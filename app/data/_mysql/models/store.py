from sqlalchemy import CHAR, Column, Integer, String
from sqlalchemy.orm import relationship

from app.data._mysql.models import BaseModel
from app.data._mysql.models.associations.stores_has_suppliers import stores_has_suppliers


class Store(BaseModel["Store"]):
    __tablename__ = "stores"

    store_id = Column(Integer, autoincrement=True, primary_key=True)
    store_type = Column(CHAR(1), nullable=False)
    phone = Column(String(25), nullable=False)
    email = Column(String(100), nullable=False)

    address = Column(String(100), nullable=True)
    zip_code = Column(String(7), nullable=True)
    city = Column(String(45), nullable=True)

    employees = relationship("Employee", back_populates="store")
    products = relationship("Storage", back_populates="store")
    suppliers = relationship(
        "Supplier",
        secondary=stores_has_suppliers,
        back_populates="stores"
    )

    @property
    def id(self) -> int:
        return self.store_id
