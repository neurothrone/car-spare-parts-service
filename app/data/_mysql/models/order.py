from sqlalchemy import Column, Date, DECIMAL, ForeignKey, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship

from app.data._mysql.models import BaseModel


class Order(BaseModel):
    __tablename__ = "orders"

    order_id = Column(Integer, autoincrement=True, primary_key=True)
    ordered_date = Column(TIMESTAMP, nullable=False)
    shipped_date = Column(TIMESTAMP, nullable=False)
    delivery_date = Column(Date)
    status = Column(String(length=15), nullable=False)

    # fk car_detail_id (one-to-one, solid)

# Many-to-Many (orders_has_products) -> OrderDetail
# class OrderDetail(Base):
#     __tablename__ = "order_details"
#
#     car_detail_id = Column(Integer, autoincrement=True, primary_key=True)
#     quantity_ordered = Column(Integer, nullable=False)
#     price_each = Column(DECIMAL(7, 2), nullable=False)
