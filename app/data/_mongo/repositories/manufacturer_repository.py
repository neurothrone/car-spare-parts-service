from __future__ import annotations
from typing import Optional

from app.data._mongo.models.manufacturer import Manufacturer
from app.data._mongo.models.product import Product
from app.data._mongo.repositories import BaseRepository


class ManufacturerRepository(BaseRepository):
    model = Manufacturer

    @classmethod
    def find_by_company_name(cls, company_name: str,
                             many: bool = False) -> Optional[Manufacturer | list[Manufacturer]]:
        return cls.find(many=many, company_name=company_name)

    @classmethod
    def find_by_head_office_phone(cls, head_office_phone: str,
                                  many: bool = False) -> Optional[Manufacturer | list[Manufacturer]]:
        return cls.find(many=many, head_office_phone=head_office_phone)

    @classmethod
    def find_by_head_office_address(cls, head_office_address: str,
                                    many: bool = False) -> Optional[Manufacturer | list[Manufacturer]]:
        return cls.find(many=many, head_office_address=head_office_address)

    @classmethod
    def add_product_to_manufacturer(cls, manufacturer: Manufacturer, product: Product) -> None:
        pass

    @classmethod
    def remove_product_from_manufacturer(cls, manufacturer: Manufacturer, product: Product) -> None:
        pass

    @classmethod
    def has_product(cls, manufacturer: Manufacturer, product: Product) -> bool:
        pass
