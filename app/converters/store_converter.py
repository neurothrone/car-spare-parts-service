from app.settings import Settings

Settings.TESTING = True

from app.data._mongo.repositories.store_repository import StoreRepository as MongoStoreRepository
from app.data._mysql.repositories.store_repository import StoreRepository as MysqlStoreRepository


class StoreConverter:
    @classmethod
    def convert_from_mysql_to_mongo(cls):
        for store in MysqlStoreRepository.find_all():
            as_dict = store.__dict__
            del as_dict["_sa_instance_state"]
            MongoStoreRepository.create(**as_dict)
