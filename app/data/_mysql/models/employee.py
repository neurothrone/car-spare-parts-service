from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.data._mysql.models import BaseModel


class Employee(BaseModel):
    __tablename__ = "employees"

    employee_id = Column(Integer, autoincrement=True, primary_key=True)

    first_name = Column(String(length=45), nullable=False)
    last_name = Column(String(length=45), nullable=False)
    phone = Column(String(length=25), nullable=False)
    email = Column(String(length=100), nullable=False)

    store_id = Column(Integer, ForeignKey("stores.store_id"))
    store = relationship("Store", back_populates="employees")
