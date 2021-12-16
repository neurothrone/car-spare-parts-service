from sqlalchemy import Column, DECIMAL, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.data._mysql.models import BaseModel


class OrderDetail(BaseModel["OrderDetail"]):
    __tablename__ = "order_details"

    order_id = Column(Integer, ForeignKey("orders.order_id"), primary_key=True, nullable=False)
    product_id = Column(Integer, ForeignKey("products.product_id"), primary_key=True, nullable=False)
    quantity_ordered = Column(Integer, nullable=False)
    price_each = Column(DECIMAL(7, 2), nullable=False)

    products = relationship("Product", back_populates="order_details")
    order = relationship("Order", back_populates="order_detail")
