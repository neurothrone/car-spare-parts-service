from app.controllers.supplier_controller import SupplierController
from generators.fake_data import FakeData
from shared.validators import validate_length


class SupplierGenerator:
    COMPANY_NAME_MAX_LEN = 45
    HEAD_OFFICE_PHONE_LEN = 25
    HEAD_OFFICE_ADDRESS_LEN = 100

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

        SupplierController.create(
            company_name=company_name,
            head_office_phone=head_office_phone,
            head_office_address=head_office_address)

    @classmethod
    def populate_database(cls, amount: int) -> None:
        phone_numbers = FakeData.generate_phone_numbers(amount)
        locations = FakeData.generate_locations(amount)
        company_names = FakeData.generate_companies(amount)

        for i in range(amount):
            cls.generate(company_name=company_names[i],
                         head_office_phone=phone_numbers[i],
                         head_office_address=locations[i].__str__())
        print("----- Supplier generated -----")


def main():
    SupplierGenerator.populate_database(amount=100)


if __name__ == "__main__":
    main()
