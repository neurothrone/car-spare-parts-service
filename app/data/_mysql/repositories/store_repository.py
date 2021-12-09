from __future__ import annotations
from typing import Optional

from app.data._mysql.db import session
from app.data._mysql.models import Product, Supplier, StoreHasProduct
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.models.store import Store


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
    def add_product_to_store(cls, store: Store,
                             product: Product,
                             stock_number: int = 0,
                             critical_threshold: int = 0,
                             amount_automatic_order: int = 0) -> None:
        if cls.has_product(store, product):
            return

        store_has_product = StoreHasProduct(stock_number=stock_number,
                                            critical_threshold=critical_threshold,
                                            amount_automatic_order=amount_automatic_order)

        store_has_product.product = product
        store.products.append(store_has_product)

        session.add(store)
        session.add(product)
        session.commit()

    @classmethod
    def has_product(cls, store: Store, product: Product) -> bool:
        for shp in store.products:
            if shp.product.product_id == product.product_id:
                return True
        return False

    @classmethod
    def remove_product_from_store(cls, store: Store, product: Product) -> None:
        if not cls.has_product(store, product):
            return

        if not store.products:
            return

        for shp in store.products:
            if shp.product.product_id == product.product_id:
                session.delete(shp)
                session.commit()
                return

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
        for supp in store.suppliers:
            if supp.supplier_id == supplier.supplier_id:
                return True
        return False
