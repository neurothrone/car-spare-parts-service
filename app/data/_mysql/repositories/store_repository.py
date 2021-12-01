from app.data._mysql.db import session
from app.data._mysql.models import Product, Manufacturer, StoreHasProduct
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.models.store import Store


class StoreRepository(BaseRepository):
    @staticmethod
    def find_by_id(_id: int) -> Store:
        return session.query(Store).filter_by(store_id=_id).first()

    @staticmethod
    def find_by_store_type(store_type: str) -> Store:
        return session.query(Store).filter_by(store_type=store_type).first()

    @staticmethod
    def find_all_by_store_type(store_type: str) -> list[Store]:
        return session.query(Store).filter_by(store_type=store_type).all()

    @staticmethod
    def add_product_to_store(store: Store,
                             product: Product,
                             stock_number: int = 0,
                             critical_threshold: int = 0,
                             amount_automatic_order: int = 0) -> None:
        if StoreRepository.has_product(store, product):
            return

        store_has_product = StoreHasProduct(stock_number=stock_number,
                                            critical_threshold=critical_threshold,
                                            amount_automatic_order=amount_automatic_order)

        store_has_product.product = product
        store.products.append(store_has_product)

        session.add(store)
        session.add(product)
        session.commit()

    @staticmethod
    def remove_product_from_store(store: Store, product: Product) -> None:
        if not StoreRepository.has_product(store, product):
            return

        if not store.products:
            return

        for shp in store.products:
            if shp.product.product_id == product.product_id:
                session.delete(shp)
                session.commit()
                return

    @staticmethod
    def add_supplier_to_store(store: Store, supplier: Manufacturer) -> None:
        if StoreRepository.has_supplier(store, supplier):
            return

        store.suppliers.append(supplier)
        session.commit()

    @staticmethod
    def remove_supplier_from_store(store: Store, supplier: Manufacturer) -> None:
        if not StoreRepository.has_supplier(store, supplier):
            return

        store.suppliers.remove(supplier)
        session.commit()

    @staticmethod
    def has_product(store: Store, product: Product) -> bool:
        for shp in store.products:
            if shp.product.product_id == product.product_id:
                return True
        return False

    @staticmethod
    def has_supplier(store: Store, supplier: Manufacturer) -> bool:
        for supp in store.suppliers:
            if supp.supplier_id == supplier.supplier_id:
                return True
        return False
