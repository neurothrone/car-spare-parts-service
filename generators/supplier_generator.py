import random
from random import randint, shuffle
from app.controllers.supplier_controller import SupplierController
from generators.fake_data import FakeData
from shared.validators import validate_length
from app.controllers.product_controller import ProductController


class SupplierGenerator:
    COMPANY_NAME_MAX_LEN = 45
    HEAD_OFFICE_PHONE_LEN = 25
    HEAD_OFFICE_ADDRESS_LEN = 100
    cpi = list(range(1, 101))

    @staticmethod
    def generate(company_name: str,
                 head_office_phone: str,
                 head_office_address: str) -> None:
        validate_length(provided=company_name,
                        limit=SupplierGenerator.COMPANY_NAME_MAX_LEN)
        validate_length(provided=head_office_phone,
                        limit=SupplierGenerator.HEAD_OFFICE_PHONE_LEN)
        validate_length(provided=head_office_address,
                        limit=SupplierGenerator.HEAD_OFFICE_ADDRESS_LEN)

        cpi_new = SupplierGenerator.cpi.pop()
        if cpi_new >= 90:
            contact_person_id = None
        else:
            contact_person_id = cpi_new

        SupplierController.create(
            company_name=company_name,
            head_office_phone=head_office_phone,
            head_office_address=head_office_address,
            contact_person_id=contact_person_id)

    @classmethod
    def populate_database(cls, amount: int) -> None:
        phone_numbers = FakeData.generate_phone_numbers(amount)
        locations = FakeData.generate_locations(amount)
        company_names = FakeData.generate_companies(amount)

        random.shuffle(SupplierGenerator.cpi)

        for i in range(amount):
            cls.generate(company_name=company_names[i],
                         head_office_phone=phone_numbers[i],
                         head_office_address=locations[i].__str__())

        print("----- Suppliers generated -----")

    @classmethod
    def add_product_to_supplier(cls, min_per_supplier: int, max_per_supplier: int) -> None:
        suppliers = SupplierController.find_all()
        products = ProductController.find_all()

        if not suppliers or not products:
            raise ValueError("No suppliers to add products to or no products to add suppliers to.")

        products_added = 0

        for supplier in suppliers:
            shuffle(products)
            products_to_add = randint(min_per_supplier, max_per_supplier)

            for index in range(products_to_add):
                SupplierController.add_product_to_supplier(supplier, products[index])
                products_added += 1

        print(f"----- {products_added} total products added to all suppliers -----")

    @classmethod
    def remove_product_from_supplier(cls) -> None:
        suppliers = SupplierController.find_all()
        products_removed = 0

        for supplier in suppliers:
            for shp in supplier.products:
                SupplierController.remove_product_from_supplier(supplier, shp.product)
                products_removed += 1

        print(f"----- {products_removed} products removed from all suppliers -----")

    @classmethod
    def print_products_in_suppliers(cls) -> None:
        suppliers = SupplierController.find_all()
        total_products = 0

        for supplier in suppliers:
            for shp in supplier.products:
                total_products += 1
                print(shp.product)
                print(shp.supplier)

        print(f"----- {total_products} total products in all suppliers -----")


def test_supplier_has_product():
    supplier = SupplierController.find_by_id(1)
    print(supplier)
    product = ProductController.find_by_id(1)

    SupplierController.add_product_to_supplier(supplier, product)
    # SupplierController.remove_product_from_supplier(supplier, product)

    for shp in supplier.products:
        print(shp.product)
        print(shp.supplier)


def test_supplier_has_contact_person():
    pass


def main():
    SupplierGenerator.populate_database(amount=100)
    # test_supplier_has_product()


if __name__ == "__main__":
    main()
