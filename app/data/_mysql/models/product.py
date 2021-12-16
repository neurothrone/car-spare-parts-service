from sqlalchemy import Column, DECIMAL, Integer, String
from sqlalchemy.orm import relationship

from app.data._mysql.models import BaseModel
from app.data._mysql.models.associations.car_details_has_products import car_details_has_products
from app.data._mysql.models.associations.products_has_manufacturers import products_has_manufacturers
from app.data._mysql.models.associations.products_has_suppliers import products_has_suppliers


class Product(BaseModel):
    __tablename__ = "products"

    product_id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(45), nullable=False)
    description = Column(String(255))
    cost = Column(DECIMAL(7, 2), nullable=False)  # CHECK (cost >= 0)
    price = Column(DECIMAL(7, 2), nullable=False)  # CHECK (price >= 0)

    stores = relationship("Storage", back_populates="product")
    order_detail = relationship("OrderDetail", back_populates="product")

    car_details = relationship(
        "CarDetail",
        secondary=car_details_has_products,
        back_populates="products"
    )
    manufacturers = relationship(
        "Manufacturer",
        secondary=products_has_manufacturers,
        back_populates="products"
    )
    suppliers = relationship(
        "Supplier",
        secondary=products_has_suppliers,
        back_populates="products"
    )

    @property
    def id(self) -> int:
        return self.product_id
