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

    stores = relationship("Storage", back_populates="product")
    order_detail = relationship("OrderDetail", back_populates="product")
