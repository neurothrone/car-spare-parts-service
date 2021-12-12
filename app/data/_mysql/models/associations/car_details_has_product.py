from sqlalchemy import Column, ForeignKey, Integer, Table

from app.data._mysql.db import Base

car_details_has_products = Table("car_details_has_products",
                                 Base.metadata,
                                 Column("car_detail_id", Integer, ForeignKey("car_detail.car_detail_id")),
                                 Column("product_id", Integer, ForeignKey("products.products_id")))
