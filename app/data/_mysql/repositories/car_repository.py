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
    def add_car_to_customer(cls, car: Car, customer: Customer) -> None:
        if cls.has_car(car, customer):
            return

        customer.cars.append(car)
        session.commit()

    @classmethod
    def remove_car_from_customer(cls, car: Car,
                                 customer: Customer) -> None:
        if not cls.has_car(car, customer):
            return

        customer.cars.remove(car)
        session.commit()

    @classmethod
    def has_car(cls, car: Car, customer: Customer) -> bool:
        if not customer.cars:
            return False

        for customer_car in customer.cars:
            if customer_car.customer_id == car.customer_id:
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
