import pprint

from app.settings import Settings

Settings.TESTING = True

from app.data._mongo.repositories.order_detail_repository import OrderDetailRepository as MongoOrderDetailRepository
from app.data._mysql.repositories.order_detail_repository import OrderDetailRepository as MysqlOrderDetailRepository


class OrderDetailConverter:
    @classmethod
    def convert_from_mysql_to_mongo(cls):
        for order_detail in MysqlOrderDetailRepository.find_all():
            as_dict = order_detail.__dict__
            as_dict = {key: value for key, value in as_dict.items() if value is not None}

            as_dict["quantity_ordered"] = order_detail.quantity_ordered
            as_dict["price_each"] = float(order_detail.product.price)

            as_dict["product"] = {
                "cost": float(order_detail.product.cost),
                "price": float(order_detail.product.price),
                "name": order_detail.product.name,
                "product_id": order_detail.product.product_id
            }

            del as_dict["product_id"]
            del as_dict["_sa_instance_state"]

            MongoOrderDetailRepository.create(**as_dict)


def main():
    OrderDetailConverter.convert_from_mysql_to_mongo()


if __name__ == "__main__":
    main()
