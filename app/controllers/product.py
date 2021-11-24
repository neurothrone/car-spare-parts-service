from app.controllers import BaseController
from app.data.models.product import Product
from app.data.repositories.product import ProductRepository


class ProductController(BaseController):
    model = Product

    @staticmethod
    def find_by_id(_id: int) -> Product:
        return ProductRepository.find_by_id(_id)
