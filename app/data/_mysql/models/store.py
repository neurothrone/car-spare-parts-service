from sqlalchemy import CHAR, Column, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship

from app.data._mysql.models import BaseModel


class StoreType:
    ONLINE = "o"
    PHYSICAL = "p"


class Store(BaseModel):
    __tablename__ = "stores"

    store_id = Column(Integer, autoincrement=True, primary_key=True)
    store_type = Column(CHAR(length=1), nullable=False)
    phone = Column(String(length=25), nullable=False)
    email = Column(String(length=100), nullable=False)

    employees = relationship("Employee", back_populates="store")

    # back_populates=StoreHasProduct.store
    products = relationship("StoreHasProduct", back_populates="store")

    # UNIQUE (store_id, store_type)


class OnlineStore:
    pass


class PhysicalStore:
    pass

# class OnlineStore(BaseModel):
#     __tablename__ = "online_stores"
#
#     store_id = Column(Integer, autoincrement=True, primary_key=True)
#     store_type = Column(CHAR(length=1), nullable=False)
#
#     # FOREIGN KEY (store_id, store_type)
#     #    REFERENCES stores (store_id, store_type) ON DELETE CASCADE
#
#
# class PhysicalStore(BaseModel):
#     __tablename__ = "physical_stores"
#
#     store_id = Column(Integer, autoincrement=True, primary_key=True)
#     store_type = Column(CHAR(length=1), nullable=False)
#     address = Column(String(length=125), nullable=False)
#     zip_code = Column(String(length=7), nullable=False)
#     city = Column(String(length=50), nullable=False)
#
#     # FOREIGN KEY (store_id, store_type)
#     #    REFERENCES stores (store_id, store_type) ON DELETE CASCADE
