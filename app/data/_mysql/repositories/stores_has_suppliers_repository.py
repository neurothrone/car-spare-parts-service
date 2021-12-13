from app.data._mysql.models.store import Store
from app.data._mysql.models.supplier import Supplier
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.repositories.store_repository import StoreRepository


class StoresHasSuppliersRepository(BaseRepository):
    model = NotImplemented

    @classmethod
    def add_supplier_to_store(cls, store: Store, supplier: Supplier) -> None:
        if cls.has_supplier(store, supplier):
            return

        store.suppliers.append(supplier)
        cls.save_many_to_db([store, supplier])

    @classmethod
    def remove_supplier_from_store(cls, store: Store, supplier: Supplier) -> None:
        if not cls.has_supplier(store, supplier):
            return

        store.suppliers.remove(supplier)
        cls.save_many_to_db([store, supplier])

    @classmethod
    def has_supplier(cls, store: Store, supplier: Supplier) -> bool:
        if not store.suppliers:
            return False

        for store_supplier in store.suppliers:
            if store_supplier.supplier_id == supplier.supplier_id:
                return True
        return False

    @classmethod
    def remove_all_suppliers_from_all_stores(cls) -> None:
        stores = StoreRepository.find_all()

        for store in stores:
            for supplier in store.suppliers:
                cls.remove_supplier_from_store(store, supplier)
