from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.data._mysql.models import BaseModel


class StoreHasProduct(BaseModel):
    __tablename__ = "stores_has_products"

    store_id = Column(Integer, ForeignKey("stores.store_id"), primary_key=True)
    product_id = Column(Integer, ForeignKey("products.product_id"), primary_key=True)

    # extra data
    stock_number = Column(Integer, default=0, nullable=False)
    critical_threshold = Column(Integer, default=0, nullable=False)
    amount_automatic_order = Column(Integer, default=0, nullable=False)

    store = relationship("Store", back_populates="products")
    product = relationship("Product", back_populates="stores")
