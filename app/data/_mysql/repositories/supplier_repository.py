from typing import Optional
from app.data._mysql.db import session
from app.data._mysql.models import ContactPerson
from app.data._mysql.models.supplier import Supplier
from app.data._mysql.models.product import Product
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.repositories.contact_person_repository import ContactPersonRepository


class SupplierRepository(BaseRepository):
    model = Supplier

    @classmethod
    def find_by_id(cls, _id: int) -> Optional[Supplier]:
        return session.query(cls.model).filter_by(supplier_id=_id).first()

    @staticmethod
    def add_product_to_supplier(supplier: Supplier,
                                product: Product) -> None:
        if SupplierRepository.has_product(supplier, product):
            return

        supplier.products.append(product)
        session.commit()

    @staticmethod
    def remove_product_from_supplier(supplier: Supplier,
                                     product: Product) -> None:
        if SupplierRepository.has_product(supplier, product):
            return

        supplier.products.remove(product)
        session.commit()

    @staticmethod
    def has_product(supplier: Supplier, product: Product) -> bool:
        for shp in supplier.products:
            if shp.product.product_id == product.product_id:
                return True
        return False
