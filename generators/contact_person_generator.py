from app.controllers.contact_person_controller import ContactPersonController
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

        print("----- Contact persons generated -----")


def main():
    ContactPersonGenerator.populate_database(amount=100)


if __name__ == "__main__":
    main()
