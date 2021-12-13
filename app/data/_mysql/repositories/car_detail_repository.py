from typing import Optional, Union
from app.data._mysql.models.product import Product
from app.data._mysql.db import session
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.models.car_detail import CarDetail


class CarDetailRepository(BaseRepository):
    model = CarDetail

    @classmethod
    def find_by_id(cls, _id: int) -> Optional[CarDetail]:
        return session.query(cls.model).filter_by(car_detail_id=_id).first()

    @classmethod
    def find_by_brand(cls, brand: str, many: bool = False) -> Optional[Union[CarDetail, list[CarDetail]]]:
        if many:
            return session.query(cls.model).filter_by(brand=brand)
        return session.query(cls.model).filter_by(brand=brand).first()

    @classmethod
    def find_by_model(cls, model: str, many: bool = False) -> Optional[Union[CarDetail, list[CarDetail]]]:
        if many:
            return session.query(cls.model).filter_by(model=model)
        return session.query(cls.model).filter_by(model=model).first()

    @classmethod
    def find_by_year(cls, year: str, many: bool = False) -> Optional[Union[CarDetail, list[CarDetail]]]:
        if many:
            return session.query(cls.model).filter_by(year=year)
        return session.query(cls.model).filter_by(year=year).first()

    @classmethod
    def add_car_detail_to_product(cls, cardetail: CarDetail,
                                  product: Product) -> None:
        if cls.has_product(cardetail, product):
            return

        cardetail.products.append(product)
        session.commit()

    @classmethod
    def remove_product_from_manufacturer(cls, cardetail: CarDetail,
                                         product: Product) -> None:
        if not cls.has_product(cardetail, product):
            return

        cardetail.products.remove(product)
        session.commit()

    @classmethod
    def has_product(cls, cardetail: CarDetail, product: Product) -> bool:
        if not cardetail.products:
            return False

        for cardetail_product in cardetail.products:
            if cardetail_product.product_id == product.product_id:
                return True
        return False
