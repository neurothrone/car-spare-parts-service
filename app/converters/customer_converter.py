from app.settings import Settings

Settings.TESTING = True

from app.data._mongo.repositories.customer_repository import CustomerRepository as MongoCustomerRepository
from app.data._mysql.repositories.customer_repository import CustomerRepository as MysqlCustomerRepository


class CustomerConverter:
    @classmethod
    def convert_from_mysql_to_mongo(cls):
        for customer in MysqlCustomerRepository.find_all():
            as_dict = customer.__dict__

            del as_dict["_sa_instance_state"]
            as_dict = {key: value for key, value in as_dict.items() if value}

            MongoCustomerRepository.create(**as_dict)
