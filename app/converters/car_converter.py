import pprint

from app.settings import Settings
from generators.car_generator import CarGenerator

Settings.TESTING = True

from app.data._mongo.repositories.car_repository import CarRepository as MongoCarRepository
from app.data._mysql.repositories.car_repository import CarRepository as MysqlCarRepository


class CarConverter:
    @classmethod
    def convert_from_mysql_to_mongo(cls):
        for car in MysqlCarRepository.find_all():
            as_dict = car.__dict__
            del as_dict["_sa_instance_state"]

            pprint.pprint(as_dict)
            quit()

            MongoCarRepository.create(**as_dict)


def main():
    # CarGenerator.generate_cars(amount=10)
    CarConverter.convert_from_mysql_to_mongo()


if __name__ == "__main__":
    main()
