from app.controllers import BaseController
from app.data.models.product import Product
from app.data.models.store import Store, StoreType
from app.data.models.supplier import Supplier
from app.data.repositories.store_repository import StoreRepository


class StoreController(BaseController):
    model = Store

    @classmethod
    def create(cls, store_type: str, phone: str, email: str,
               address: str = None, zip_code: str = None, city: str = None) -> None:
        if store_type not in [StoreType.PHYSICAL, StoreType.ONLINE]:
            raise ValueError("Store type can only be 'p' or 'o'.")

        if store_type == StoreType.PHYSICAL and None in [address, zip_code, city]:
            raise TypeError("A physical store must have an address, zip code or city.")

        if store_type == StoreType.ONLINE and None not in [address, zip_code, city]:
            raise TypeError("An online store must not have an address, zip code or city.")

        StoreRepository.create(cls.model,
                               store_type=store_type, phone=phone,
                               email=email, address=address,
                               zip_code=zip_code, city=city)

    @staticmethod
    def find_by_id(_id: int) -> Store:
        return StoreRepository.find_by_id(_id)

    @staticmethod
    def find_by_store_type(store_type: str) -> Store:
        return StoreRepository.find_by_store_type(store_type)

    @staticmethod
    def find_all_by_store_type(store_type: str) -> list[Store]:
        return StoreRepository.find_all_by_store_type(store_type)

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
