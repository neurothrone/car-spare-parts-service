from __future__ import annotations
from typing import Optional

from app.data._mysql.db import session
from app.data._mysql.models.supplier import Supplier
from app.data._mysql.models.product import Product
from app.data._mysql.repositories import BaseRepository


class SupplierRepository(BaseRepository):
    model = Supplier

    @classmethod
    def find_by_id(cls, _id: int) -> Optional[Supplier]:
        return session.query(cls.model).filter_by(supplier_id=_id).first()

    @classmethod
    def find_by_company_name(cls, company_name: str,
                             many: bool = False) -> Optional[Supplier | list[Supplier]]:
        if many:
            return session.query(cls.model).filter_by(company_name=company_name)
        return session.query(cls.model).filter_by(company_name=company_name).first()

    @classmethod
    def find_by_head_office_phone(cls, head_office_phone: str,
                                  many: bool = False) -> Optional[Supplier | list[Supplier]]:
        if many:
            return session.query(cls.model).filter_by(head_office_phone=head_office_phone)
        return session.query(cls.model).filter_by(head_office_phone=head_office_phone).first()

    @classmethod
    def find_by_head_office_address(cls, head_office_address: str,
                                    many: bool = False) -> Optional[Supplier | list[Supplier]]:
        if many:
            return session.query(cls.model).filter_by(head_office_address=head_office_address)
        return session.query(cls.model).filter_by(head_office_address=head_office_address).first()

    @classmethod
    def add_product_to_supplier(cls, supplier: Supplier,
                                product: Product) -> None:
        if cls.has_product(supplier, product):
            return

        supplier.products.append(product)
        session.commit()

    @classmethod
    def remove_product_from_supplier(cls, supplier: Supplier,
                                     product: Product) -> None:
        if not cls.has_product(supplier, product):
            return

        supplier.products.remove(product)
        session.commit()

    @classmethod
    def has_product(cls, supplier: Supplier, product: Product) -> bool:
        if not supplier.products:
            return False

        for supplier_product in supplier.products:
            if supplier_product.product_id == product.product_id:
                return True
        return False
