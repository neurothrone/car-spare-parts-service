from __future__ import annotations

from typing import Optional
from app.data._mysql.db import session
from app.data._mysql.models import products_has_suppliers
from app.data._mysql.models.supplier import Supplier
from app.data._mysql.models.product import Product
from app.data._mysql.repositories import BaseRepository


class SupplierRepository(BaseRepository):
    model = Supplier

    @classmethod
    def find_by_id(cls, _id: int) -> Optional[Supplier]:
        return session.query(cls.model).filter_by(supplier_id=_id).first()

    @classmethod
    def find_by_company_name(cls, company_name: str, many: bool = False) -> Optional[Supplier | list[Supplier]]:
        if many:
            return session.query(cls.model).filter_by(company_name=company_name)
        return session.query(cls.model).filter_by(company_name=company_name).first()

    @classmethod
    def find_by_head_office_phone(cls, head_office_phone: str, many: bool = False) -> Optional[
        Supplier | list[Supplier]]:
        if many:
            return session.query(cls.model).filter_by(head_office_phone=head_office_phone)
        return session.query(cls.model).filter_by(head_office_phone=head_office_phone).first()

    @classmethod
    def find_by_head_office_address(cls, head_office_address: str, many: bool = False) -> Optional[
        Supplier | list[Supplier]]:
        if many:
            return session.query(cls.model).filter_by(head_office_address=head_office_address)
        return session.query(cls.model).filter_by(head_office_address=head_office_address).first()

    @staticmethod
    def add_product_to_supplier(supplier: Supplier,
                                product: Product) -> None:
        if SupplierRepository.has_product(supplier, product):
            return
        supplier_has_product = products_has_suppliers()

        supplier_has_product.product = product
        supplier.products.append(supplier_has_product)

        session.add(supplier)
        session.add(product)
        session.commit()

    @staticmethod
    def remove_product_from_supplier(supplier: Supplier,
                                     product: Product) -> None:
        if not SupplierRepository.has_product(supplier, product):
            return

        if not supplier.products:
            return

        for mhp in supplier.products:
            if mhp.product.product_id == product.product_id:
                session.delete(mhp)
                session.commit()
                return

    @staticmethod
    def has_product(supplier: Supplier, product: Product) -> bool:
        for shp in supplier.products:
            if shp.product.product_id == product.product_id:
                return True
        return False
