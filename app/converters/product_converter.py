from app.settings import Settings

Settings.TESTING = True

from app.data._mongo.repositories.product_repository import ProductRepository as MongoProductRepository
from app.data._mysql.repositories.product_repository import ProductRepository as MysqlProductRepository


class ProductConverter:
    @classmethod
    def convert_from_mysql_to_mongo(cls):
        for product in MysqlProductRepository.find_all():
            as_dict = product.__dict__
            as_dict["cost"] = float(as_dict["cost"])
            as_dict["price"] = float(as_dict["price"])
            del as_dict["_sa_instance_state"]
            MongoProductRepository.create(**as_dict)


def main():
    ProductConverter.convert_from_mysql_to_mongo()


if __name__ == '__main__':
    main()
