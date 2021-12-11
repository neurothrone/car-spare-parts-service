from __future__ import annotations
from typing import Optional
from app.data._mysql.db import session
from app.data._mysql.models import ManufacturerHasProduct
from app.data._mysql.models.manufacturer import Manufacturer
from app.data._mysql.models.product import Product
from app.data._mysql.repositories import BaseRepository


class ManufacturerRepository(BaseRepository):
    model = Manufacturer

    @classmethod
    def find_by_id(cls, _id: int) -> Optional[Manufacturer]:
        return session.query(cls.model).filter_by(manufacturer_id=_id).first()

    @classmethod
    def find_by_company_name(cls, company_name: str, many: bool = False) -> Optional[Manufacturer | list[Manufacturer]]:
        if many:
            return session.query(cls.model).filter_by(company_name=company_name)
        return session.query(cls.model).filter_by(company_name=company_name).first()

    @classmethod
    def find_by_head_office_phone(cls, head_office_phone: str, many: bool = False) -> Optional[Manufacturer | list[Manufacturer]]:
        if many:
            return session.query(cls.model).filter_by(head_office_phone=head_office_phone)
        return session.query(cls.model).filter_by(head_office_phone=head_office_phone).first()

    @classmethod
    def find_by_head_office_address(cls, head_office_address: str, many: bool = False) -> Optional[Manufacturer | list[Manufacturer]]:
        if many:
            return session.query(cls.model).filter_by(head_office_address=head_office_address)
        return session.query(cls.model).filter_by(head_office_address=head_office_address).first()

    @staticmethod
    def add_product_to_manufacturer(manufacturer: Manufacturer,
                                    product: Product) -> None:
        if ManufacturerRepository.has_product(manufacturer, product):
            return
        manufacturer_has_product = ManufacturerHasProduct()

        manufacturer_has_product.product = product
        manufacturer.products.append(manufacturer_has_product)

        session.add(manufacturer)
        session.add(product)
        session.commit()

    @staticmethod
    def remove_product_from_manufacturer(manufacturer: Manufacturer,
                                         product: Product) -> None:
        if not ManufacturerRepository.has_product(manufacturer, product):
            return

        if not manufacturer.products:
            return

        for mhp in manufacturer.products:
            if mhp.product.product_id == product.product_id:
                session.delete(mhp)
                session.commit()
                return

    @staticmethod
    def has_product(manufacturer: Manufacturer, product: Product) -> bool:
        for mhp in manufacturer.products:
            if mhp.product.product_id == product.product_id:
                return True
        return False
