from sqlalchemy import Column, Date, Integer, String, TIMESTAMP

from app.data._mysql.models import BaseModel


class Order(BaseModel):
    __tablename__ = "orders"

    order_id = Column(Integer, autoincrement=True, primary_key=True)
    ordered_date = Column(TIMESTAMP, nullable=False)
    shipped_date = Column(TIMESTAMP, nullable=False)
    delivery_date = Column(Date)
    status = Column(String(15), nullable=False)
