from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.data._mysql.models import BaseModel


class StoreHasProduct(BaseModel):
    __tablename__ = "stores_has_products"

    store_id = Column(Integer, ForeignKey("stores.store_id"), primary_key=True)
    product_id = Column(Integer, ForeignKey("products.product_id"), primary_key=True)

    stock_number = Column(Integer, default=0, nullable=False)
    critical_threshold = Column(Integer, default=0, nullable=False)
    amount_automatic_order = Column(Integer, default=0, nullable=False)

    store = relationship("Store", back_populates="products")
    product = relationship("Product", back_populates="stores")

    def __init__(self, stock_number: int = 0, critical_threshold: int = 0,
                 amount_automatic_order: int = 0) -> None:
        self.stock_number = stock_number
        self.critical_threshold = critical_threshold
        self.amount_automatic_order = amount_automatic_order

    def __repr__(self) -> str:
        return f"StoreHasProduct: {self.stock_number}, {self.critical_threshold}, {self.amount_automatic_order}"
