from app.settings import Settings
Settings.TESTING = True
from converters.contact_person_converter import ContactPersonConverter
from converters.product_converter import ProductConverter
from converters.store_converter import StoreConverter
from converters.manufacturer_converter import ManufacturerConverter
from converters.supplier_converter import SupplierConverter


def main():
    ContactPersonConverter.convert_from_mysql_to_mongo()
    ProductConverter.convert_from_mysql_to_mongo()
    StoreConverter.convert_from_mysql_to_mongo()
    SupplierConverter.convert_from_mysql_to_mongo()
    ManufacturerConverter.convert_from_mysql_to_mongo()


if __name__ == '__main__':
    main()
