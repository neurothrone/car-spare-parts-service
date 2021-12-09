from __future__ import annotations
from typing import Optional

from app.controllers import BaseController
from app.data.models.contact_person import ContactPerson
from app.data.models.product import Product
from app.data.models.supplier import Supplier
from app.data.repositories.supplier_repository import SupplierRepository


class SupplierController(BaseController):
    repository = SupplierRepository
    required_attributes = {"company_name", "head_office_phone",
                           "head_office_address", "contact_person_id"}

    @classmethod
    def find_by_id(cls, _id: int | str) -> Optional[Supplier]:
        return cls.repository.find_by_id(_id)

    # region Supplier-ContactPerson

    @classmethod
    def add_contact_person(cls, supplier: Supplier, contact_person: ContactPerson) -> None:
        cls.repository.add_contact_person(supplier, contact_person)

    @classmethod
    def remove_contact_person(cls, supplier: Supplier) -> None:
        cls.repository.remove_contact_person(supplier)

    @classmethod
    def has_contact_person(cls, supplier: Supplier) -> bool:
        return supplier.contact_person_id is not None

    # endregion Supplier-ContactPerson

    # region Supplier-Product

    @classmethod
    def add_product_to_supplier(cls, supplier: Supplier,
                                product: Product) -> None:
        cls.repository.add_product_to_supplier(supplier, product)

    @classmethod
    def remove_product_from_supplier(cls, supplier: Supplier,
                                     product: Product) -> None:
        cls.repository.remove_product_from_supplier(supplier, product)

    @classmethod
    def has_supplier(cls, contact_person: ContactPerson) -> bool:
        return contact_person.supplier is not None

    # endregion Supplier-Product
