from sqlalchemy import Column, Integer, String

from app.data._mysql.models import BaseModel


class CarDetail(BaseModel):
    __tablename__ = "car_details"

    car_detail_id = Column(Integer, autoincrement=True, primary_key=True)
    brand = Column(String(45), nullable=False)
    model = Column(String(45), nullable=False)
    year = Column(Integer, nullable=False)
