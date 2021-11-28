from sqlalchemy import CHAR, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.data._mysql.models import BaseModel
from app.data._mysql.models.associations.store_has_supplier import stores_has_suppliers


class StoreType:
    ONLINE = "o"
    PHYSICAL = "p"


class Store(BaseModel):
    __tablename__ = "stores"

    store_id = Column(Integer, autoincrement=True, primary_key=True)
    store_type = Column(CHAR(length=1), nullable=False)
    phone = Column(String(length=25), nullable=False)
    email = Column(String(length=100), nullable=False)

    address = Column(String(length=100), nullable=True)
    zip_code = Column(String(length=7), nullable=True)
    city = Column(String(length=45), nullable=True)

    employees = relationship("Employee", back_populates="store")
    products = relationship("StoreHasProduct", back_populates="store")
    suppliers = relationship(
        "Supplier",
        secondary=stores_has_suppliers,
        back_populates="stores"
    )

# TODO:
#       - remove Not Null constraint from address, zip_code, city
#       - when creating a store, if store_type is online, only then can address, zip and city be null
#       - update repository, controller, generator and add safeguard/differentiation for online, physical type
#       - verify new changes work on generators and so on
