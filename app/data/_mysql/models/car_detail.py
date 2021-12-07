from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.data._mysql.models import BaseModel


class CarDetail(BaseModel):
    __tablename__ = "car_details"

    car_detail_id = Column(Integer, autoincrement=True, primary_key=True)
    brand = Column(String(45), nullable=False)
    model = Column(String(45), nullable=False)
    year = Column(Integer, nullable=False)

    car = relationship("Car", back_populates="car_detail", uselist=False)
    product = relationship("OrderDetail", back_populates="products")
