from typing import Optional, Union
from app.data._mysql.models.car_detail import CarDetail
from app.data._mysql.db import session
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.models.customer import Customer


class CustomerRepository(BaseRepository):
    model = Customer

    @classmethod
    def find_by_id(cls, _id: int) -> Optional[Customer]:
        return session.query(cls.model).filter_by(customer_id=_id).first()

    @classmethod
    def find_by_customer_type(cls, customer_type: str,
                              many: bool = False) -> Optional[Union[Customer, list[Customer]]]:
        if many:
            return session.query(cls.model).filter_by(customer_type=customer_type)
        return session.query(cls.model).filter_by(customer_type=customer_type).first()

    @classmethod
    def find_by_customer_name(cls, customer_name: str,
                              many: bool = False) -> Optional[Union[Customer, list[Customer]]]:
        if many:
            return session.query(cls.model).filter_by(customer_name=customer_name)
        return session.query(cls.model).filter_by(customer_name=customer_name).first()

    @classmethod
    def find_by_contact_first_name(cls, contact_first_name: str,
                                   many: bool = False) -> Optional[Union[Customer, list[Customer]]]:
        if many:
            return session.query(cls.model).filter_by(contact_first_name=contact_first_name)
        return session.query(cls.model).filter_by(contact_first_name=contact_first_name).first()

    @classmethod
    def find_by_contact_last_name(cls, contact_last_name: str,
                                  many: bool = False) -> Optional[Union[Customer, list[Customer]]]:
        if many:
            return session.query(cls.model).filter_by(contact_last_name=contact_last_name)
        return session.query(cls.model).filter_by(contact_last_name=contact_last_name).first()

    @classmethod
    def find_by_phone(cls, phone: str, many: bool = False) -> Optional[Union[Customer, list[Customer]]]:
        if many:
            return session.query(cls.model).filter_by(phone=phone)
        return session.query(cls.model).filter_by(phone=phone).first()

    @classmethod
    def find_by_email(cls, email: str, many: bool = False) -> Optional[Union[Customer, list[Customer]]]:
        if many:
            return session.query(cls.model).filter_by(email=email)
        return session.query(cls.model).filter_by(email=email).first()

    @classmethod
    def find_by_address(cls, address: str, many: bool = False) -> Optional[Union[Customer, list[Customer]]]:
        if many:
            return session.query(cls.model).filter_by(address=address)
        return session.query(cls.model).filter_by(address=address).first()

    @classmethod
    def find_by_zip_code(cls, zip_code: str, many: bool = False) -> Optional[Union[Customer, list[Customer]]]:
        if many:
            return session.query(cls.model).filter_by(zip_code=zip_code)
        return session.query(cls.model).filter_by(zip_code=zip_code).first()

    @classmethod
    def find_by_city(cls, city: str, many: bool = False) -> Optional[Union[Customer, list[Customer]]]:
        if many:
            return session.query(cls.model).filter_by(city=city)
        return session.query(cls.model).filter_by(city=city).first()

    @classmethod
    def add_car_detail_to_customer(cls, customer: Customer, car_detail: CarDetail) -> None:
        if cls.has_car_detail(customer, car_detail):
            return

        customer.car_details.append(car_detail)
        session.commit()

    @classmethod
    def remove_customer_from_car(cls, customer: Customer, car_detail: CarDetail) -> None:
        if not cls.has_car_detail(customer, car_detail):
            return

        customer.car_details.remove(car_detail)
        session.commit()

    @classmethod
    def has_car_detail(cls, customer: Customer, car_detail: CarDetail) -> bool:
        if not customer.car_details:
            return False

        for customer_car_detail in customer.car_details:
            if customer_car_detail.car_detail_id == car_detail.car_detail_id:
                return True
        return False
