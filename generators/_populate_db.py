from app.settings import Settings
Settings.TESTING = True
from generators.contact_person_generator import ContactPersonGenerator
from generators.manufacturer_generator import ManufacturerGenerator
from generators.supplier_generator import SupplierGenerator
from generators.product_has_manufacturer_generator import ManufacturerHasProductGenerator
from generators.product_has_supplier_generator import SupplierHasProductGenerator
from generators.store_has_supplier_generator import StoreHasSupplierGenerator


def main():
    ContactPersonGenerator.populate_database(amount=10)
    SupplierGenerator.populate_database(amount=10)
    ManufacturerGenerator.populate_database(amount=10)
    ManufacturerHasProductGenerator.populate_database(amount=10)
    SupplierHasProductGenerator.populate_database(amount=10)
    StoreHasSupplierGenerator.populate_database(amount=10)


if __name__ == "__main__":
    main()
