from app.settings import Settings

Settings.TESTING = True

from app.data._mongo.repositories.order_detail_repository import OrderDetailRepository as MongoOrderDetailRepository
from app.data._mysql.repositories.order_detail_repository import OrderDetailRepository as MysqlOrderDetailRepository

class ProductConverter:
    @classmethod
    def convert_from_mysql_to_mongo(cls):
        for order_detail in MysqlOrderDetailRepository.find_all():
            as_dict = order_detail.__dict__
            as_dict["quantity ordered"] = str(as_dict["quantity ordered"])
            as_dict["price each"] = float(as_dict["price each"])
            del as_dict["_sa_instance_state"]
            MongoOrderDetailRepository.create(**as_dict)


def main():
    if __name__ == '__main__':
        main()
