from __future__ import annotations
from typing import Optional
from app.data.models.car_detail import CarDetail
from app.controllers import BaseController
from app.data.models.customer import Customer
from app.data.repositories.customer_repository import CustomerRepository


class CustomerController(BaseController):
    repository = CustomerRepository
    required_attributes = {
        "customer_type", "customer_name", "contact_first_name",
        "contact_last_name", "phone", "email", "address",
        "zip_code", "city", "employee_id"
    }

    @classmethod
    def create(cls, customer_type: str, customer_name: str,
               contact_first_name: str, contact_last_name: str, phone: str,
               email: str, address: str, zip_code: str, city: str,
               employee_id: Optional[int | str] = None) -> None:
        cls.repository.create(customer_type=customer_type, customer_name=customer_name,
                              contact_first_name=contact_first_name, contact_last_name=contact_last_name,
                              phone=phone, email=email, address=address, zip_code=zip_code,
                              city=city, employee_id=employee_id)

    @classmethod
    def find_by_id(cls, _id: int | str) -> Optional[Customer]:
        return CustomerRepository.find_by_id(_id)

    @classmethod
    def find_by_customer_type(cls, customer_type) -> Optional[Customer]:
        return cls.repository.find_by_customer_type(customer_type)

    @classmethod
    def find_by_customer_name(cls, customer_name: str) -> Optional[Customer]:
        return cls.repository.find_by_customer_name(customer_name)

    @classmethod
    def find_by_contact_first_name(cls, contact_first_name: str) -> Optional[Customer]:
        return cls.repository.find_by_contact_first_name(contact_first_name)

    @classmethod
    def find_by_contact_last_name(cls, contact_last_name: str) -> Optional[Customer]:
        return cls.repository.find_by_contact_last_name(contact_last_name)

    @classmethod
    def find_phone(cls, phone: str) -> Optional[Customer]:
        return cls.repository.find_by_phone(phone)

    @classmethod
    def find_by_email(cls, email: str) -> Optional[Customer]:
        return cls.repository.find_by_email(email)

    @classmethod
    def find_by_address(cls, address: str) -> Optional[Customer]:
        return cls.repository.find_by_address(address)

    @classmethod
    def find_by_zip_code(cls, zip_code: str) -> Optional[Customer]:
        return cls.repository.find_by_address(zip_code)

    @classmethod
    def find_by_city(cls, city: str) -> Optional[Customer]:
        return cls.repository.find_by_city(city)

    @classmethod
    def add_car_detail_to_customer(cls, customer: Customer, car_detail: CarDetail) -> None:
        cls.repository.add_car_detail_to_customer(customer, car_detail)

    @classmethod
    def remove_customer_from_car(cls, customer: Customer, car_detail: CarDetail) -> None:
        cls.repository.remove_customer_from_car(customer, car_detail)
