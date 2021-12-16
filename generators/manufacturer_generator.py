from app.settings import Settings, Database
Settings.TESTING = True
import random
from app.controllers.contact_person_controller import ContactPersonController
from app.controllers.manufacturer_controller import ManufacturerController
from generators.fake_data import FakeData
from shared.validators import validate_length


class ManufacturerGenerator:
    COMPANY_NAME_MAX_LEN = 45
    HEAD_OFFICE_PHONE_LEN = 25
    HEAD_OFFICE_ADDRESS_LEN = 100

    @staticmethod
    def generate(company_name: str, head_office_phone: str, head_office_address: str, contact_person_id: int) -> None:
        validate_length(provided=company_name, limit=ManufacturerGenerator.COMPANY_NAME_MAX_LEN)
        validate_length(provided=head_office_phone, limit=ManufacturerGenerator.HEAD_OFFICE_PHONE_LEN)
        validate_length(provided=head_office_address, limit=ManufacturerGenerator.HEAD_OFFICE_ADDRESS_LEN)

        ManufacturerController.create(company_name=company_name,
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

        print(f"----- {amount} Manufacturers generated -----")

    @classmethod
    def print_products_in_manufacturer(cls) -> None:
        manufacturers = ManufacturerController.find_all()
        total_products = 0

        for manufacturer in manufacturers:
            for mhp in manufacturer.products:
                total_products += 1
                print(mhp.product)
                print(mhp.manufacturer)

        print(f"----- {total_products} total products in manufacturers -----")


def main():
    ManufacturerGenerator.populate_database(amount=5)


if __name__ == "__main__":
    main()
