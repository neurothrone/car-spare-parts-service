from typing import Optional
from app.data.models.car_detail import CarDetail
from app.controllers import BaseController
from app.data.models.product import Product
from app.data.repositories.product_repository import ProductRepository


class ProductController(BaseController):
    repository = ProductRepository
    required_attributes = {"name", "description", "cost", "price"}

    @classmethod
    def create(cls, name: str, description: str, cost: float, price: float) -> None:
        ProductRepository.create(name=name, description=description,
                                 cost=cost, price=price)

    @staticmethod
    def find_by_id(_id: int) -> Optional[Product]:
        return ProductRepository.find_by_id(_id)

    @classmethod
    def find_by_name(cls, name: str) -> Optional[Product]:
        return cls.repository.find_by_name(name)

    @classmethod
    def find_by_city(cls, city: str) -> Optional[Product]:
        return cls.repository.find_by_city(city)

    @classmethod
    def find_by_cost(cls, cost: str) -> Optional[Product]:
        return cls.repository.find_by_cost(cost)

    @classmethod
    def find_by_price(cls, price: str) -> Optional[Product]:
        return cls.repository.find_by_price(price)

    @classmethod
    def add_car_detail_to_product(cls, product: Product, car_detail: CarDetail) -> None:
        cls.repository.add_car_detail_to_product(product, car_detail)

    @classmethod
    def remove_car_detail_from_product(cls, product: Product, car_detail: CarDetail) -> None:
        cls.repository.remove_car_detail_from_product(product, car_detail)
