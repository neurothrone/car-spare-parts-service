from sqlalchemy import Column, Integer, String

from app.data._mysql.models import BaseModel


class Car(BaseModel):
    __tablename__ = "cars"

    # car_id = Column(Integer, autoincrement=True, primary_key=True)
    reg_no = Column(String(length=7), primary_key=True)
    color = Column(String(length=45))

    # fk car_detail_id (one-to-one, solid)


class CarDetail(BaseModel):
    __tablename__ = "car_details"

    car_detail_id = Column(Integer, autoincrement=True, primary_key=True)
    brand = Column(String(length=45), nullable=False)
    model = Column(String(length=45), nullable=False)
    year = Column(Integer, nullable=False)
