from app.controllers import BaseController
from app.data.models.product import Product
from app.data.models.supplier import Supplier
from app.data.repositories.products_has_suppliers_repository import ProductsHasSuppliersRepository


class ProductsHasSuppliersController(BaseController):
    repository = ProductsHasSuppliersRepository

    @classmethod
    def add_product_to_supplier(cls, product: Product,
                                supplier: Supplier) -> None:
        cls.repository.add_product_to_supplier(product, supplier)

    @classmethod
    def remove_product_from_supplier(cls, product: Product,
                                     supplier: Supplier) -> None:
        cls.repository.remove_product_from_supplier(product, supplier)
