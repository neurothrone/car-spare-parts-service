from app.controllers import BaseController
from app.data.models.product import Product
from app.data.repositories.product import ProductRepository


class ProductController(BaseController):
    model = Product

    @classmethod
    def create(cls, name: str, description: str, cost: float, price: float) -> Product:
        return ProductRepository.create(cls.model, name=name, description=description,
                                        cost=cost, price=price)

    @staticmethod
    def find_by_id(_id: int) -> Product:
        return ProductRepository.find_by_id(_id)
