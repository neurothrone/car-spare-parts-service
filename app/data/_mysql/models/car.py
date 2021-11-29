from sqlalchemy import Column, String

from app.data._mysql.models import BaseModel


class Car(BaseModel):
    __tablename__ = "cars"

    reg_no = Column(String(length=7), primary_key=True)
    color = Column(String(length=45))
