from __future__ import annotations
from typing import Optional

from app.controllers import BaseController
from app.data.models.product import Product
from app.data.models.store import Store
from app.data.models.supplier import Supplier
from app.data.repositories.store_repository import StoreRepository
from shared.models.types import StoreType


class StoreController(BaseController):
    repository = StoreRepository
    required_attributes = {"store_type", "phone", "email", "address", "zip_code", "city"}

    @classmethod
    def create(cls, store_type: str, phone: str, email: str,
               address: str = None, zip_code: str = None, city: str = None) -> None:
        if store_type not in [StoreType.PHYSICAL, StoreType.ONLINE]:
            raise ValueError("Store type can only be 'p' or 'o'.")

        if store_type == StoreType.PHYSICAL and None in [address, zip_code, city]:
            raise TypeError("A physical store must have an address, zip code or city.")

        if store_type == StoreType.ONLINE and None not in [address, zip_code, city]:
            raise TypeError("An online store must not have an address, zip code or city.")

        cls.repository.create(store_type=store_type, phone=phone,
                              email=email, address=address,
                              zip_code=zip_code, city=city)

    @classmethod
    def create_many(cls, data: list[dict]) -> None:
        for store_data in data:
            cls.validate(store_data)

        for store_data in data:
            cls.create(**store_data)

    @classmethod
    def find_by_id(cls, _id: int | str) -> Optional[Store]:
        return cls.repository.find_by_id(_id)

    @classmethod
    def find_by_city(cls, city: str) -> Optional[Store]:
        return cls.repository.find_by_city(city)

    @classmethod
    def find_by_email(cls, email: str) -> Optional[Store]:
        return cls.repository.find_by_email(email)

    @classmethod
    def find_by_store_type(cls, store_type: str) -> Store:
        return cls.repository.find_by_store_type(store_type)

    @classmethod
    def find_all_by_store_type(cls, store_type: str) -> list[Store]:
        return cls.repository.find_by_store_type(store_type, many=True)

    # region Store-Product

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

    # endregion Store-Product

    # region Store-Supplier

    @classmethod
    def add_supplier_to_store(cls, store: Store, supplier: Supplier) -> None:
        cls.repository.add_supplier_to_store(store, supplier)

    @classmethod
    def remove_supplier_from_store(cls, store: Store, supplier: Supplier) -> None:
        cls.repository.remove_supplier_from_store(store, supplier)

    # endregion Store-Supplier
