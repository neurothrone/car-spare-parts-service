from __future__ import annotations
from typing import Optional

from app.data._mongo.models.store import Store
from app.data._mongo.models.product import Product
from app.data._mongo.models.storage import Storage
from app.data._mongo.models.supplier import Supplier
from app.data._mongo.repositories import BaseRepository


class StoreRepository(BaseRepository):
    model = Store

    # region Store

    @classmethod
    def find_by_city(cls, city: str, many: bool = False) -> Optional[Store | list[Store]]:
        return cls.find(many=many, city=city)

    @classmethod
    def find_by_email(cls, email: str, many: bool = False) -> Optional[Store | list[Store]]:
        return cls.find(many=many, email=email)

    @classmethod
    def find_by_store_type(cls, store_type: str, many: bool = False) -> Optional[Store | list[Store]]:
        return cls.find(many=many, store_type=store_type)

    # endregion Store

    # region Stores-Products

    @staticmethod
    def add_product_to_store(store: Store,
                             product: Product,
                             stock_number: int = 0,
                             critical_threshold: int = 0,
                             amount_automatic_order: int = 0) -> None:
        pass

    @staticmethod
    def remove_product_from_store(store: Store, product: Product) -> None:
        pass

    @staticmethod
    def has_product(store: Store, product: Product) -> bool:
        pass

    # endregion Stores-Products

    # region Stores-Suppliers

    @staticmethod
    def add_supplier_to_store(store: Store, supplier: Supplier) -> None:
        pass

    @staticmethod
    def remove_supplier_from_store(store: Store, supplier: Supplier) -> None:
        pass

    @staticmethod
    def has_supplier(store: Store, supplier: Supplier) -> bool:
        pass

    # endregion Stores-Suppliers
