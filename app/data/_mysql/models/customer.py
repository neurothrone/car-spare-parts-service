from sqlalchemy import CHAR, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.data._mysql.models import BaseModel


class Customer(BaseModel):
    __abstract__ = True

    customer_id = Column(Integer, autoincrement=True, primary_key=True)

    # CHECK (customer_type IN ('c', 'p'))
    customer_type = Column(CHAR(1), nullable=False)
    customer_name = Column(String(100), nullable=False)
    phone = Column(String(25), nullable=False)
    email = Column(String(100), nullable=False)
    address = Column(String(100), nullable=False)
    zip_code = Column(String(7), nullable=False)
    city = Column(String(50), nullable=False)

    # customer One-to-Many (optional) order
    # employee (optional) One-to-Many (optional) customer
    # customer One-to-Many (optional) car
