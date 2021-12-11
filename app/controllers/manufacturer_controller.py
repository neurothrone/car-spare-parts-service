from __future__ import annotations
from app.controllers import BaseController
from app.data.models.manufacturer import Manufacturer
from app.data.repositories.manufacturer_repository import ManufacturerRepository
from app.data.models.product import Product
from typing import Optional


class ManufacturerController(BaseController):
    repository = ManufacturerRepository
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
    def find_by_id(cls, _id: Optional[int | str]) -> Optional[Manufacturer]:
        return cls.repository.find_by_id(_id)

    @classmethod
    def find_by_company_name(cls, company_name: str) -> Optional[Manufacturer]:
        return cls.repository.find_by_company_name(company_name)

    @classmethod
    def find_by_head_office_phone(cls, head_office_phone: str) -> Optional[Manufacturer]:
        return cls.repository.find_by_head_office_phone(head_office_phone)

    @classmethod
    def find_by_head_office_address(cls, head_office_address: str) -> Optional[Manufacturer]:
        return cls.repository.find_by_head_office_address(head_office_address)

    @classmethod
    def add_product_to_manufacturer(cls, manufacturer: Manufacturer,
                                    product: Product) -> None:
        cls.repository.add_product_to_manufacturer(manufacturer, product)

    @classmethod
    def remove_product_from_manufacturer(cls, manufacturer: Manufacturer,
                                         product: Product) -> None:
        cls.repository.remove_product_from_manufacturer(manufacturer, product)
