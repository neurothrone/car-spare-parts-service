from sqlalchemy import Column, DECIMAL, Integer

from app.data._mysql.models import BaseModel


class OrderDetail(BaseModel):
    __tablename__ = "order_details"

    car_detail_id = Column(Integer, autoincrement=True, primary_key=True)
    quantity_ordered = Column(Integer, nullable=False)
    price_each = Column(DECIMAL(7, 2), nullable=False)
