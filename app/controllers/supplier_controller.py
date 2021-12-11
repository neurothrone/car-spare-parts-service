from __future__ import annotations
from typing import Optional
from app.controllers import BaseController
from app.data.models.supplier import Supplier
from app.data.models.product import Product
from app.data.repositories.supplier_repository import SupplierRepository


class SupplierController(BaseController):
    repository = SupplierRepository
    required_attributes = {"company_name", "head_office_phone",
                           "head_office_address", "contact_person_id"}

    @classmethod
    def create(cls, company_name: str, head_office_phone: str, head_office_address: str,
               contact_person_id: Optional[int | str] = None) -> None:
        cls.repository.create(company_name=company_name,
                              head_office_phone=head_office_phone,
                              head_office_address=head_office_address,
                              contact_person_id=contact_person_id)

    @classmethod
    def find_by_id(cls, _id: Optional[int | str]) -> Optional[Supplier]:
        return cls.repository.find_by_id(_id)

    @classmethod
    def find_by_company_name(cls, company_name: str) -> Optional[Supplier]:
        return cls.repository.find_by_company_name(company_name)

    @classmethod
    def find_by_head_office_phone(cls, head_office_phone: str) -> Optional[Supplier]:
        return cls.repository.find_by_head_office_phone(head_office_phone)

    @classmethod
    def find_by_head_office_address(cls, head_office_address: str) -> Optional[Supplier]:
        return cls.repository.find_by_head_office_address(head_office_address)

    @classmethod
    def add_product_to_supplier(cls, supplier: Supplier,
                                product: Product) -> None:
        cls.repository.add_product_to_supplier(supplier, product)

    @classmethod
    def remove_product_from_supplier(cls, supplier: Supplier,
                                     product: Product) -> None:
        cls.repository.remove_product_from_supplier(supplier, product)
