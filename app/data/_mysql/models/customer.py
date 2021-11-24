from sqlalchemy import CHAR, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.data._mysql.models import BaseModel


class Customer(BaseModel):
    __abstract__ = True

    customer_id = Column(Integer, autoincrement=True, primary_key=True)

    # CHECK (customer_type IN ('c', 'p'))
    customer_type = Column(CHAR(length=1), nullable=False)
    customer_name = Column(String(length=100), nullable=False)
    phone = Column(String(length=25), nullable=False)
    email = Column(String(length=100), nullable=False)
    address = Column(String(length=125), nullable=False)
    zip_code = Column(String(length=7), nullable=False)
    city = Column(String(length=50), nullable=False)

    # fk employee_id @ employees table
    # UNIQUE (customer_id, customer_type)


class CorporateCustomer(BaseModel):
    __tablename__ = "customers"

    customer_id = Column(Integer, autoincrement=True, primary_key=True)
    customer_type = Column(CHAR(length=1), nullable=False)
    organization_number = Column(Integer, nullable=False, unique=True)
    organization_name = Column(String(length=45), nullable=False)

    # customer_id         INT AUTO_INCREMENT PRIMARY KEY,
    # customer_type       CHAR(1) NOT NULL DEFAULT 'c' check (customer_type = 'c'),
    # organization_number INT     NOT NULL UNIQUE,
    # organization_name   VARCHAR(45) NOT NULL

    # FOREIGN KEY (customer_id, customer_type)
    # REFERENCES customers (customer_id, customer_type) ON DELETE CASCADE
    pass


class PrivateCustomer(BaseModel):
    __tablename__ = "customers"

    customer_id = Column(Integer, autoincrement=True, primary_key=True)
    customer_type = Column(CHAR(length=1), nullable=False)
    first_name = Column(String(length=45), nullable=False)
    last_name = Column(String(length=45), nullable=False)

    # customer_id   INT AUTO_INCREMENT PRIMARY KEY,
    # customer_type CHAR(1)     NOT NULL DEFAULT 'p' check (customer_type = 'p'),
    # first_name    VARCHAR(45) NOT NULL,
    # last_name     VARCHAR(45) NOT NULL,

    # FOREIGN KEY (customer_id, customer_type)
    # REFERENCES customers (customer_id, customer_type) ON DELETE CASCADE
    pass
