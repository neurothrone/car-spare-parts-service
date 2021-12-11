from app.data._mysql.db import session
from app.data._mysql.models.product import Product
from app.data._mysql.models.storage import Storage
from app.data._mysql.models.store import Store
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.repositories.store_repository import StoreRepository


class StorageRepository(BaseRepository):
    model = Storage

    @classmethod
    def add_product_to_store(cls, store: Store,
                             product: Product,
                             stock_number: int = 0,
                             critical_threshold: int = 0,
                             amount_automatic_order: int = 0) -> None:
        if cls.has_product(store, product):
            return

        storage = Storage(stock_number=stock_number,
                          critical_threshold=critical_threshold,
                          amount_automatic_order=amount_automatic_order)

        storage.product = product
        store.products.append(storage)

        session.add(store)
        session.add(product)
        session.commit()

    @classmethod
    def has_product(cls, store: Store, product: Product) -> bool:
        for storage in store.products:
            if storage.product.product_id == product.product_id:
                return True
        return False

    @classmethod
    def remove_product_from_store(cls, store: Store, product: Product) -> None:
        if not cls.has_product(store, product):
            return

        if not store.products:
            return

        for storage in store.products:
            if storage.product.product_id == product.product_id:
                session.delete(storage)
                session.commit()
                return

    @classmethod
    def remove_all_products_from_all_stores(cls) -> None:
        stores = StoreRepository.find_all()

        for store in stores:
            for storage in store.products:
                cls.remove_product_from_store(store, storage.product)
