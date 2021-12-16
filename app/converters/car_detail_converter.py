from app.data._mongo.repositories.car_detail_repository import CarDetailRepository as MongoProductRepository
from app.data._mysql.repositories.car_detail_repository import CarDetailRepository as MysqlProductRepository


from app.settings import Settings

Settings.TESTING = True


class CarDetailConverter:
    @classmethod
    def convert_from_mysql_to_mongo(cls):
        for car_detail in MysqlProductRepository.find_all():
            as_dict = car_detail.__dict__
            del as_dict["_sa_instance_state"]
            MongoProductRepository.create(**as_dict)


def main():
    if __name__ == '__main__':
        main()
