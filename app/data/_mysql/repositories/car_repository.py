from typing import Optional, Union
from app.data._mysql.models.car_detail import CarDetail
from app.data._mysql.db import session
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.models.car import Car
from app.data._mysql.models.customer import Customer


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
    def add_car_detail_to_car(cls, car: Car, car_detail: CarDetail) -> None:
        if cls.has_car_detail(car, car_detail):
            return

        car.car_details.append(car_detail)
        session.commit()

    @classmethod
    def remove_car_detail_from_car(cls, car: Car,
                                   car_detail: CarDetail) -> None:
        if not cls.has_car_detail(car, car_detail):
            return

        car.car_details.remove(car_detail)
        session.commit()

    @classmethod
    def add_customer_to_car(cls, car: Car, customer: Customer) -> None:
        if cls.has_customer(car, customer):
            return

        car.customers.append(customer)
        session.commit()

    @classmethod
    def remove_customer_from_car(cls, car: Car,
                                 customer: Customer) -> None:
        if not cls.has_customer(car, customer):
            return

        car.customers.remove(customer)
        session.commit()

    @classmethod
    def has_customer(cls, car: Car, customer: Customer) -> bool:
        if not car.customers:
            return False

        for car_customer in car.customers:
            if car_customer.customer_id == customer.customer_id:
                return True
        return False

    @classmethod
    def has_car_detail(cls, car: Car, car_detail: CarDetail) -> bool:
        if not car.car_details:
            return False

        for car_car_detail in car.car_details:
            if car_car_detail.car_detail_id == car_detail.car_detail_id:
                return True
        return False
