from typing import Optional, Union

from app.data._mysql.db import session
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.models.car import Car
from app.data._mysql.models.customer import Customer
from app.data._mysql.repositories.customer_repository import CustomerRepository


class CarRepository(BaseRepository):
    model = Car

    @classmethod
    def find_by_reg_no(cls, reg_no: str) -> Optional[Car]:
        return session.query(cls.model).filter_by(reg_no=reg_no).first()

    @classmethod
    def find_by_color(cls, color: str, many: bool = False) -> Optional[Union[Car, list[Car]]]:
        if many:
            return session.query(cls.model).filter_by(color=color)
        return session.query(cls.model).filter_by(color=color).first()

    @classmethod
    def add_customer(cls, car: Car, customer: Customer) -> None:
        if cls.has_customer(car) or CarRepository.has_car_details(customer):
            return
        car.customer_id = customer.customer_id
        customer.car = car
        session.commit()

    @classmethod
    def has_customer(cls, car: Car) -> bool:
        return car.customer_id is not None

    @classmethod
    def has_car_details(cls, customer: Customer) -> bool:
        return customer.car is not None

    @classmethod
    def remove_customer(cls, car: Car) -> None:
        if not cls.has_customer(car):
            return

        customer = CustomerRepository.find_by_id(car.customer_id)
        customer.car = None
        car.customer_id = None
        session.commit()
