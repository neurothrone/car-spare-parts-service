from app.data._mongo.repositories.car_repository import CarRepository as MongoProductRepository
from app.data._mysql.repositories.car_repository import CarRepository as MysqlProductRepository


from app.settings import Settings

Settings.TESTING = True


class CarConverter:
    @classmethod
    def convert_from_mysql_to_mongo(cls):
        for car in MysqlProductRepository.find_all():
            as_dict = car.__dict__
            del as_dict["_sa_instance_state"]
            MongoProductRepository.create(**as_dict)


def main():
    if __name__ == '__main__':
        main()
