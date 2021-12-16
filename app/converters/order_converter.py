from app.settings import Settings

Settings.TESTING = True

from app.data._mongo.repositories.order_repository import OrderRepository as MongoOrderRepository
from app.data._mysql.repositories.order_repository import OrderRepository as MysqlOrderRepository
from app.data._mongo.repositories.customer_repository import CustomerRepository as MongoCustomerRepository


class OrderConverter:
    @classmethod
    def convert_from_mysql_to_mongo(cls):
        for order in MysqlOrderRepository.find_all():
            as_dict = order.__dict__
            as_dict = {key: str(value) for key, value in as_dict.items() if value is not None}
            as_dict['customer_id'] = MongoCustomerRepository.find(customer_id=order.customer.customer_id)._id

            del as_dict["_sa_instance_state"]
        #
        # for order_detail in MysqlOrderDetailRepository.find_all():
        #     as_dict = order_detail.__dict__
        #     as_dict = {key: value for key, value in as_dict.items() if value is not None}
        #



            # products = []
            # for product in order.products:
            #     products.append({
            #         "cost": float(product.cost),
            #         "price": float(product.price),
            #         "name": product.name,
            #         "product_id": product.product_id
            #     })
        #
        #     order_details = []
        #     for order_detail in order_details:
        #         order_details.append({
        #             "quantity_ordered": float(order_detail.quantity_ordered),
        #             "price_each": float(order_detail.price_each)
        #         })
        #
            # as_dict['products'] = products
        #     as_dict['order_details'] = order_details

            MongoOrderRepository.create(**as_dict)


def main():
    OrderConverter.convert_from_mysql_to_mongo()


if __name__ == '__main__':
    main()
