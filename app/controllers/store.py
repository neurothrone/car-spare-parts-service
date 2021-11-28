from app.controllers import BaseController
from app.data.models.product import Product
from app.data.models.store import Store
from app.data.models.supplier import Supplier
from app.data.repositories.store import StoreRepository


class StoreController(BaseController):
    model = Store

    @classmethod
    def create(cls, store_type: str, phone: str, email: str) -> Store:
        return StoreRepository.create(cls.model, store_type=store_type, phone=phone,
                                      email=email)

    @staticmethod
    def find_by_id(_id: int) -> Store:
        return StoreRepository.find_by_id(_id)

    @staticmethod
    def add_product_to_store(store: Store, product: Product,
                             stock_number: int = 0,
                             critical_threshold: int = 0,
                             amount_automatic_order: int = 0) -> None:
        StoreRepository.add_product_to_store(store, product, stock_number,
                                             critical_threshold, amount_automatic_order)

    @staticmethod
    def remove_product_from_store(store: Store, product: Product) -> None:
        StoreRepository.remove_product_from_store(store, product)

    @staticmethod
    def add_supplier_to_store(store: Store, supplier: Supplier) -> None:
        StoreRepository.add_supplier_to_store(store, supplier)

    @staticmethod
    def remove_supplier_from_store(store: Store, supplier: Supplier) -> None:
        StoreRepository.remove_supplier_from_store(store, supplier)
