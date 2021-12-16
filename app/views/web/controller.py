from app.controllers.car_controller import CarController
from app.controllers.car_detail_controller import CarDetailController
from app.controllers.customer_controller import CustomerController
from app.controllers.employee_controller import EmployeeController
from app.controllers.product_controller import ProductController
from app.controllers.storage_controller import StorageController
from app.controllers.store_controller import StoreController
from app.converters.car_converter import CarConverter
from app.converters.customer_converter import CustomerConverter
from app.converters.product_converter import ProductConverter
from app.converters.storage_converter import StorageConverter
from app.converters.store_converter import StoreConverter
from app.data._mongo.db import drop_mongo_db
from app.data._mysql.repositories.product_repository import ProductRepository as MysqlProductRepository
from app.data._mysql.repositories.storage_repository import StorageRepository as MysqlStorageRepository
from app.data._mysql.repositories.store_repository import StoreRepository as MysqlStoreRepository
from generators.car_generator import CarGenerator
from generators.customer_generator import CustomerGenerator
from generators.employee_generator import EmployeeGenerator
from generators.product_generator import ProductGenerator
from generators.storage_generator import StorageGenerator
from generators.store_generator import StoreGenerator


class WebController:
    @staticmethod
    def populate_mysql_db():
        StoreGenerator.populate_database(amount=10)
        EmployeeGenerator.populate_database(amount=30)
        EmployeeController.connect_employees_to_stores(min_=1, max_=3)

        CustomerGenerator.populate_database(amount=30)
        CarGenerator.generate_cars(amount=30)
        CustomerGenerator.add_cars_to_customers()

        # TODO: order

        ProductGenerator.populate_database(amount=50)
        StorageGenerator.add_products_to_stores(min_per_store=1, max_per_store=5)

    @staticmethod
    def convert_mysql_to_mongo():
        ProductConverter.convert_from_mysql_to_mongo()
        StoreConverter.convert_from_mysql_to_mongo()

        for product, store in zip(MysqlProductRepository.find_all(), MysqlStoreRepository.find_all()):
            MysqlStorageRepository.add_product_to_store(store, product)

        StorageConverter.convert_from_mysql_to_mongo()

        CustomerConverter.convert_from_mysql_to_mongo()
        CarConverter.convert_from_mysql_to_mongo()

    @staticmethod
    def delete_data_from_mysql_db():
        CarController.delete_all()
        CarDetailController.delete_all()
        StorageController.delete_all()
        CustomerController.delete_all()
        EmployeeController.delete_all()
        ProductController.delete_all()
        StoreController.delete_all()

    @staticmethod
    def delete_data_from_mongo_db():
        drop_mongo_db("car-spare-parts-mongo-db-test")
