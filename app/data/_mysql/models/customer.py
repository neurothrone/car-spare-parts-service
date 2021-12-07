from sqlalchemy import CHAR, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.data._mysql.models import BaseModel


class Customer(BaseModel):
    __tablename__ = "customers"

    customer_id = Column(Integer, autoincrement=True, primary_key=True)
    customer_type = Column(CHAR(length=1), nullable=False)  # CHECK (customer_type IN ('c', 'p'))
    customer_name = Column(String(length=100), nullable=True)
    contact_first_name = Column(String(length=45), nullable=True)
    contact_last_name = Column(String(length=45), nullable=True)
    phone = Column(String(length=25), nullable=False)
    email = Column(String(length=100), nullable=False)
    address = Column(String(length=100), nullable=False)
    zip_code = Column(String(length=7), nullable=False)
    city = Column(String(length=50), nullable=False)

    employee_id = Column(Integer, ForeignKey("employees.employee_id"))
    employee = relationship("Employee", back_populates="customers")
    order = relationship("Order", back_populates="customer")
    # customer One-to-Many (optional) order
    # customer One-to-Many (optional) car
