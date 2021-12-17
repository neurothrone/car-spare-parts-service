from app.settings import Settings

Settings.TESTING = True

from app.data._mongo.repositories.order_detail_repository import OrderDetailRepository as MongoOrderDetailRepository
from app.data._mysql.repositories.order_detail_repository import OrderDetailRepository as MysqlOrderDetailRepository

from controllers.order_detail_controller import OrderDetailController
# from data._mongo.repositories.order_repository import OrderRepository as MongoOrderRepository


class OrderDetailConverter:
    @classmethod
    def convert_from_mysql_to_mongo(cls):
        for order_detail in MysqlOrderDetailRepository.find_all():
            as_dict = order_detail.__dict__
            as_dict = {key: str(value) for key, value in as_dict.items() if value is not None}
            # as_dict['contact_person_id'] = MongoOrderRepository.find(contact_person_id=manufacturer.contact_person_id)._id

            order_detail = OrderDetailController.find_by_id(order_detail.order_detail_id)
            as_dict["quantity_ordered"] = order_detail.quantity_ordered
            as_dict["price_each"] = order_detail.price_each

            del as_dict["_sa_instance_state"]

            products = []
            for product in order_detail.products:
                products.append({
                    "cost": float(product.cost),
                    "price": float(product.price),
                    "name": product.name,
                    "product_id": product.product_id
                })

            as_dict['products'] = products

            MongoOrderDetailRepository.create(**as_dict)
