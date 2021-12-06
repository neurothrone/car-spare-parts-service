from app.controllers.contact_person_controller import ContactPersonController
from app.controllers.supplier_controller import SupplierController
from generators.fake_data import FakeData
from shared.validators import validate_length


class ContactPersonGenerator:
    COMPANY_NAME_MAX_LEN = 45
    FIRST_NAME_MAX_LEN = 45
    LAST_NAME_MAX_LEN = 45
    PHONE_MAX_LEN = 25
    EMAIL_MAX_LEN = 100

    @staticmethod
    def generate(first_name: str, last_name: str, phone: str, email: str) -> None:
        validate_length(provided=first_name, limit=ContactPersonGenerator.FIRST_NAME_MAX_LEN)
        validate_length(provided=last_name, limit=ContactPersonGenerator.LAST_NAME_MAX_LEN)
        validate_length(provided=phone, limit=ContactPersonGenerator.PHONE_MAX_LEN)
        validate_length(provided=email, limit=ContactPersonGenerator.EMAIL_MAX_LEN)

        ContactPersonController.create(
            first_name=first_name, last_name=last_name,
            phone=phone, email=email)

    @classmethod
    def populate_database(cls, amount: int) -> None:
        full_names = FakeData.generate_full_names(amount, unique=True)
        phone_numbers = FakeData.generate_phone_numbers(amount)
        emails = FakeData.generate_emails(full_names, amount)

        for i in range(amount):
            first_name, last_name = full_names[i].split(" ")
            cls.generate(
                first_name=first_name,
                last_name=last_name,
                phone=phone_numbers[i],
                email=emails[i]
            )

        print(f"----- {amount} Contact Persons generated -----")


def test_supplier_contact_person():
    contact_person = ContactPersonController.find_by_id(1)
    supplier = SupplierController.find_by_id(1)

    print(contact_person)
    print(supplier)

    print()
    print(contact_person.supplier)
    print(f"Supplier, contact_person_id: {supplier.contact_person_id}")

    SupplierController.add_contact_person(supplier, contact_person)
    # SupplierController.remove_contact_person(supplier)

    print()
    print(contact_person.supplier)
    print(f"Supplier, contact_person_id: {supplier.contact_person_id}")


def main():
    ContactPersonGenerator.populate_database(amount=100)
    # TODO: populate suppliers
    # test_supplier_contact_person()


if __name__ == "__main__":
    main()
