from app.controllers import BaseController
from app.data.models.product import Product
from app.data.models.store import Store
from app.data.repositories.storage_repository import StorageRepository


class StorageController(BaseController):
    repository = StorageRepository
    required_attributes = {"stock_number",
                           "critical_threshold",
                           "amount_automatic_order"}

    @classmethod
    def add_product_to_store(cls, store: Store, product: Product,
                             stock_number: int = 0,
                             critical_threshold: int = 0,
                             amount_automatic_order: int = 0) -> None:
        cls.repository.add_product_to_store(store, product, stock_number,
                                            critical_threshold, amount_automatic_order)

    @classmethod
    def remove_product_from_store(cls, store: Store, product: Product) -> None:
        cls.repository.remove_product_from_store(store, product)

    @classmethod
    def remove_all_products_from_all_stores(cls) -> None:
        cls.repository.remove_all_products_from_all_stores()
