from sqlalchemy import Column, Date, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship

from app.data._mysql.models import BaseModel


class Order(BaseModel):
    __tablename__ = "orders"

    order_id = Column(Integer, autoincrement=True, primary_key=True)
    ordered_date = Column(TIMESTAMP, nullable=False)
    shipped_date = Column(TIMESTAMP, nullable=False)
    delivery_date = Column(Date,nullable=True)
    status = Column(String(15), nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"), nullable=True)

    customer = relationship("Customer", back_populates="orders")
    order_detail = relationship("OrderDetail", back_populates="order")
