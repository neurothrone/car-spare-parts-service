from sqlalchemy import Column, DECIMAL, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.data._mysql.models import BaseModel


class Product(BaseModel):
    __tablename__ = "products"

    product_id = Column(Integer, autoincrement=True, primary_key=True)

    name = Column(String(length=45), nullable=False)
    description = Column(String(length=255))

    # CHECK (cost >= 0)
    cost = Column(DECIMAL(7, 2), nullable=False)
    # CHECK (price >= 0)
    price = Column(DECIMAL(7, 2), nullable=False)

    # CONSTRAINT products_chk_price_gt_cost
    #   CHECK (price >= cost)
