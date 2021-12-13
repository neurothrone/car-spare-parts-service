from typing import Optional, Union
from app.data._mysql.models.car_detail import CarDetail
from app.data._mysql.db import session
from app.data._mysql.repositories import BaseRepository
from app.data._mysql.models.product import Product


class ProductRepository(BaseRepository):
    model = Product

    @classmethod
    def find_by_id(cls, _id: int) -> Optional[Product]:
        return session.query(cls.model).filter_by(product_id=_id).first()

    @classmethod
    def find_by_name(cls, name: str, many: bool = False) -> Optional[Union[Product, list[Product]]]:
        if many:
            return session.query(cls.model).filter_by(name=name)
        return session.query(cls.model).filter_by(name=name).first()

    @classmethod
    def find_by_city(cls, description: str, many: bool = False) -> Optional[Union[Product, list[Product]]]:
        if many:
            return session.query(cls.model).filter_by(description=description)
        return session.query(cls.model).filter_by(description=description).first()

    @classmethod
    def find_by_cost(cls, cost: str, many: bool = False) -> Optional[Union[Product, list[Product]]]:
        if many:
            return session.query(cls.model).filter_by(cost=cost)
        return session.query(cls.model).filter_by(cost=cost).first()

    @classmethod
    def find_by_price(cls, price: str, many: bool = False) -> Optional[Union[Product, list[Product]]]:
        if many:
            return session.query(cls.model).filter_by(price=price)
        return session.query(cls.model).filter_by(price=price).first()

    @classmethod
    def add_car_detail_to_product(cls, product: Product, car_detail: CarDetail) -> None:
        if cls.has_product(product, car_detail):
            return

        product.car_details.append(car_detail)
        session.commit()

    @classmethod
    def remove_car_detail_from_product(cls, product: Product, car_detail: CarDetail) -> None:
        if not cls.has_product(product, car_detail):
            return

        product.car_details.remove(car_detail)
        session.commit()

    @classmethod
    def has_product(cls, product: Product, car_detail: CarDetail) -> bool:
        if not product.car_details:
            return False

        for product_car_detail in product.car_details:
            if product_car_detail.car_detail_id == car_detail.car_detail_id:
                return True
        return False
