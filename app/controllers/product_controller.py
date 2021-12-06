from typing import Optional

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
