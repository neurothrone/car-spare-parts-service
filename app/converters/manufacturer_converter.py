from app.settings import Settings

Settings.TESTING = True

from app.data._mongo.repositories.manufacturer_repository import ManufacturerRepository as MongoManufacturerRepository
from app.data._mysql.repositories.manufacturer_repository import ManufacturerRepository as MysqlManufacturerRepository


class ManufacturerConverter:
    @classmethod
    def convert_from_mysql_to_mongo(cls):
        for manufacturer in MysqlManufacturerRepository.find_all():
            as_dict = manufacturer.__dict__
            del as_dict["_sa_instance_state"]
            as_dict = {key: value for key, value in as_dict.items() if value is not None}
            print()
            MongoManufacturerRepository.create(**as_dict)
