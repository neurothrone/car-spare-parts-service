from sqlalchemy import Column, Integer, String

from app.data._mysql.models import BaseModel


class Manufacturer(BaseModel):
    __tablename__ = "manufacturers"

    manufacturer_id = Column(Integer, autoincrement=True, primary_key=True)
    company_name = Column(String(length=45), nullable=False)
    head_office_phone = Column(String(length=25), nullable=False)
    head_office_address = Column(String(length=100), nullable=False)
