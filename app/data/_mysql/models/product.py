from sqlalchemy import Column, DECIMAL, Integer, String
from sqlalchemy.orm import relationship

from app.data._mysql.models import BaseModel


class Product(BaseModel):
    __tablename__ = "products"

    product_id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(45), nullable=False)
    description = Column(String(255))
    cost = Column(DECIMAL(7, 2), nullable=False)  # CHECK (cost >= 0)
    price = Column(DECIMAL(7, 2), nullable=False)  # CHECK (price >= 0)

    stores = relationship("StoreHasProduct", back_populates="product")
    order_details = relationship("OrderDetail", back_populates="product")
    car_details_has_products = relationship("Car_details_has_products", back_populates="product")
