from app.settings import Settings

Settings.TESTING = True

from app.controllers.car_controller import CarController
from app.controllers.car_detail_controller import CarDetailController
from app.controllers.customer_controller import CustomerController
from app.converters.customer_converter import CustomerConverter
from app.data._mongo.repositories.car_repository import CarRepository as MongoCarRepository
from app.data._mysql.repositories.car_repository import CarRepository as MysqlCarRepository
from app.data._mongo.repositories.customer_repository import CustomerRepository as MongoCustomerRepository
from generators.car_generator import CarGenerator
from generators.customer_generator import CustomerGenerator


class CarConverter:
    @classmethod
    def convert_from_mysql_to_mongo(cls):
        for car in MysqlCarRepository.find_all():
            as_dict = car.__dict__
            customer = MongoCustomerRepository.find(customer_id=car.customer_id)

            as_dict["customer_id"] = customer._id
            car_detail = CarDetailController.find_by_id(car.car_detail_id)
            as_dict["model"] = car_detail.model
            as_dict["brand"] = car_detail.brand
            as_dict["year"] = car_detail.year

            del as_dict["car_detail_id"]
            del as_dict["_sa_instance_state"]

            MongoCarRepository.create(**as_dict)


def delete_all():
    CarController.delete_all()
    CarDetailController.delete_all()
    CustomerController.delete_all()


def main():
    # delete_all()

    # MySQL Setup
    CarGenerator.generate_cars(amount=10)
    CustomerGenerator.populate_database(amount=10)

    cars = CarController.find_all()
    customers = CustomerController.find_all()

    for car, customer in zip(cars, customers):
        CarController.add_car_to_customer(car, customer)

    # Mongo Conversion
    # CustomerConverter.convert_from_mysql_to_mongo()
    CarConverter.convert_from_mysql_to_mongo()


if __name__ == "__main__":
    main()
