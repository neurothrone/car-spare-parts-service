import random

from app.settings import Settings, Database

Settings.TESTING = True

from app.controllers.contact_person_controller import ContactPersonController
from app.controllers.supplier_controller import SupplierController
from generators.fake_data import FakeData
from shared.validators import validate_length


class SupplierGenerator:
    COMPANY_NAME_MAX_LEN = 45
    HEAD_OFFICE_PHONE_LEN = 25
    HEAD_OFFICE_ADDRESS_LEN = 100

    @staticmethod
    def generate(company_name: str, head_office_phone: str, head_office_address: str, contact_person_id: int) -> None:
        validate_length(provided=company_name, limit=SupplierGenerator.COMPANY_NAME_MAX_LEN)
        validate_length(provided=head_office_phone, limit=SupplierGenerator.HEAD_OFFICE_PHONE_LEN)
        validate_length(provided=head_office_address, limit=SupplierGenerator.HEAD_OFFICE_ADDRESS_LEN)

        SupplierController.create(company_name=company_name,
                                  head_office_phone=head_office_phone,
                                  head_office_address=head_office_address,
                                  contact_person_id=contact_person_id)

    @classmethod
    def populate_database(cls, amount: int) -> None:
        phone_numbers = FakeData.generate_phone_numbers(amount)
        locations = FakeData.generate_locations(amount)
        company_names = FakeData.generate_companies(amount)

        for i in range(amount):

            if Settings.DATABASE == Database.MONGO:
                pass

            else:
                contact_person_id = random.choice(ContactPersonController.find_all()).contact_person_id

                cls.generate(company_name=company_names[i],
                             head_office_phone=phone_numbers[i],
                             head_office_address=locations[i].__str__(),
                             contact_person_id=contact_person_id)

        print(f"----- {amount} Suppliers generated -----")

    @classmethod
    def print_products_in_supplier(cls) -> None:
        suppliers = SupplierController.find_all()[0]
        total_products = 0

        for supplier in suppliers:
            for shp in supplier.products:
                total_products += 1
                print(shp.product)
                print(shp.supplier)

        print(f"----- {total_products} total products in one supplier -----")

    @classmethod
    def all_suppliers_to_dict(cls) -> list[dict]:
        suppliers = []
        for supplier in SupplierController.find_all():
            data = supplier.__dict__
            if supplier.contact_person_id:
                contact_person = ContactPersonController.find_by_id(supplier.contact_person_id)
                data |= contact_person.__dict__
            del data["_sa_instance_state"]
            suppliers.append(data)
        return suppliers


def main():
    SupplierGenerator.populate_database(amount=5)


if __name__ == "__main__":
    main()
