from __future__ import annotations
from typing import Optional

from app.data._mysql.db import session
from app.data._mysql.models.store import Store
from app.data._mysql.models.supplier import Supplier
from app.data._mysql.repositories import BaseRepository


class StoreRepository(BaseRepository):
    model = Store

    @classmethod
    def find_by_id(cls, _id: int) -> Optional[Store]:
        return session.query(cls.model).filter_by(store_id=_id).first()

    @classmethod
    def find_by_city(cls, city: str, many: bool = False) -> Optional[Store | list[Store]]:
        if many:
            return session.query(cls.model).filter_by(city=city)
        return session.query(cls.model).filter_by(city=city).first()

    @classmethod
    def find_by_email(cls, email: str, many: bool = False) -> Optional[Store | list[Store]]:
        if many:
            return session.query(cls.model).filter_by(email=email)
        return session.query(cls.model).filter_by(email=email).first()

    @classmethod
    def find_by_store_type(cls, store_type: str, many: bool = False) -> Optional[Store | list[Store]]:
        if many:
            return session.query(cls.model).filter_by(store_type=store_type)
        return session.query(cls.model).filter_by(store_type=store_type).first()

    @classmethod
    def add_supplier_to_store(cls, store: Store, supplier: Supplier) -> None:
        if cls.has_supplier(store, supplier):
            return

        store.suppliers.append(supplier)
        session.commit()

    @classmethod
    def remove_supplier_from_store(cls, store: Store, supplier: Supplier) -> None:
        if not cls.has_supplier(store, supplier):
            return

        store.suppliers.remove(supplier)
        session.commit()

    @classmethod
    def has_supplier(cls, store: Store, supplier: Supplier) -> bool:
        if not store.suppliers:   # hasattr(store, "suppliers")
            return False

        for store_supplier in store.suppliers:
            if store_supplier.supplier_id == supplier.supplier_id:
                return True
        return False

    @classmethod
    def remove_all_suppliers_from_all_stores(cls) -> None:
        stores = cls.find_all()

        for store in stores:
            for supplier in store.suppliers:
                cls.remove_supplier_from_store(store, supplier)
