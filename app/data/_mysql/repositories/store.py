from app.data._mysql.db import session
from app.data._mysql.models import Supplier
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.models.store import Store


class StoreRepository(BaseRepository):
    @staticmethod
    def find_by_id(_id: int) -> Store:
        return session.query(Store).filter_by(store_id=_id).first()

    @staticmethod
    def add_supplier_to_store(store: Store, supplier: Supplier) -> None:
        if StoreRepository.has_supplier(store, supplier):
            return
        store.suppliers.append(supplier)
        session.commit()

    @staticmethod
    def remove_supplier_from_store(store: Store, supplier: Supplier) -> None:
        if not StoreRepository.has_supplier(store, supplier):
            return
        store.suppliers.remove(supplier)
        session.commit()

    @staticmethod
    def has_supplier(store: Store, supplier: Supplier) -> bool:
        for supp in store.suppliers:
            if supp.supplier_id == supplier.supplier_id:
                return True
        return False
