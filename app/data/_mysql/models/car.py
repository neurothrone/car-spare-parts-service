from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.data._mysql.models import BaseModel


class Car(BaseModel):
    __tablename__ = "cars"

    reg_no = Column(String(7), primary_key=True)
    color = Column(String(45), nullable=True)
    car_detail_id = Column(Integer, ForeignKey("car_details.car_detail_id"), primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"), nullable=True)

    customer = relationship("Customer", back_populates="cars")
    car_detail = relationship("CarDetail", back_populates="car")
