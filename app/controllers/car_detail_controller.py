from __future__ import annotations
from typing import Optional
from app.data.models.product import Product
from app.controllers import BaseController
from app.data.models.car_detail import CarDetail
from app.data.repositories.car_detail_repository import CarDetailRepository


class CarDetailController(BaseController):
    repository = CarDetailRepository
    required_attributes = {"brand", "model", "year"}

    @classmethod
    def create(cls, brand: str, model: str, year: str) -> None:
        CarDetailRepository.create(brand=brand, model=model, year=year)

    @classmethod
    def find_by_id(cls, _id: int | str) -> Optional[CarDetail]:
        return CarDetailRepository.find_by_id(_id)

    @classmethod
    def find_by_brand(cls, brand: str) -> Optional[CarDetail]:
        return cls.repository.find_by_brand(brand)

    @classmethod
    def find_by_model(cls, model: str) -> Optional[CarDetail]:
        return cls.repository.find_by_model(model)

    @classmethod
    def find_by_year(cls, year: str) -> Optional[CarDetail]:
        return cls.repository.find_by_year(year)

    @classmethod
    def add_car_detail_to_product(cls, car_detail: CarDetail, product: Product) -> None:
        cls.repository.add_car_detail_to_product(car_detail, product)

    @classmethod
    def remove_car_detail(cls, car_detail: CarDetail, product: Product) -> None:
        cls.repository.remove_car_detail_from_product(car_detail, product)
