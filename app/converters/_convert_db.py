from app.settings import Settings

Settings.TESTING = True
from converters.contact_person_converter import ContactPersonConverter
from converters.product_converter import ProductConverter
from converters.store_converter import StoreConverter
from converters.manufacturer_converter import ManufacturerConverter
from converters.supplier_converter import SupplierConverter
# from converters.car_converter import CarConverter
# from converters.customer_converter import CustomerConverter
from converters.storage_converter import StorageConverter


def main():
    ContactPersonConverter.convert_from_mysql_to_mongo()
    ProductConverter.convert_from_mysql_to_mongo()
    StoreConverter.convert_from_mysql_to_mongo()
    StorageConverter.convert_from_mysql_to_mongo()
    SupplierConverter.convert_from_mysql_to_mongo()
    ManufacturerConverter.convert_from_mysql_to_mongo()
    # CustomerConverter.convert_from_mysql_to_mongo()
    # CarConverter.convert_from_mysql_to_mongo()


if __name__ == '__main__':
    main()
