from typing import Optional, Union

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
