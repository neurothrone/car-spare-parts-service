from random import randint
from typing import Optional

from app.controllers.customer_controller import CustomerController
from app.data.models.customer import CustomerType
from generators.fake_data import FakeData
from shared.validators import validate_length


class CustomerGenerator:
    CUSTOMER_TYPE_MAX_LEN = 1
    CUSTOMER_NAME_MAX_LEN = 100
    CONTACT_FIRST_NAME_MAX_LEN = 45
    CONTACT_LAST_NAME_MAX_LEN = 45
    PHONE_MAX_LEN = 25
    EMAIL_MAX_LEN = 100
    ADDRESS_MAX_LEN = 100
    ZIP_CODE_MAX_LEN = 7
    CITY_MAX_LEN = 50

    @classmethod
    def generate(cls,
                 customer_type: str,
                 customer_name: Optional[str],
                 contact_first_name: Optional[str],
                 contact_last_name: Optional[str],
                 phone: str,
                 email: str,
                 address: str,
                 zip_code: str,
                 city: str) -> None:

        validate_length(customer_type, cls.CUSTOMER_TYPE_MAX_LEN)
        if customer_name:
            validate_length(customer_name, cls.CUSTOMER_NAME_MAX_LEN)
        if contact_first_name:
            validate_length(contact_first_name, cls.CONTACT_FIRST_NAME_MAX_LEN)
        if contact_last_name:
            validate_length(contact_last_name, cls.CONTACT_LAST_NAME_MAX_LEN)
        validate_length(phone, cls.PHONE_MAX_LEN)
        validate_length(email, cls.EMAIL_MAX_LEN)
        validate_length(address, cls.ADDRESS_MAX_LEN)
        validate_length(zip_code, cls.ZIP_CODE_MAX_LEN)
        validate_length(city, cls.CITY_MAX_LEN)

        CustomerController.create(
            customer_type=customer_type,
            customer_name=customer_name,
            contact_first_name=contact_first_name,
            contact_last_name=contact_last_name,
            phone=phone,
            email=email,
            address=address,
            zip_code=zip_code,
            city=city
        )

    @classmethod
    def generate_corporate_customer(cls,
                                    customer_name: str,
                                    phone: str,
                                    email: str,
                                    address: str,
                                    zip_code: str,
                                    city: str) -> None:
        cls.generate(
            customer_type=CustomerType.CORPORATE,
            customer_name=customer_name,
            contact_first_name=None,
            contact_last_name=None,
            phone=phone,
            email=email,
            address=address,
            zip_code=zip_code,
            city=city
        )

    @classmethod
    def generate_private_customer(cls,
                                  contact_first_name: str,
                                  contact_last_name: str,
                                  phone: str,
                                  email: str,
                                  address: str,
                                  zip_code: str,
                                  city: str) -> None:
        cls.generate(
            customer_type=CustomerType.PRIVATE,
            customer_name=None,
            contact_first_name=contact_first_name,
            contact_last_name=contact_last_name,
            phone=phone,
            email=email,
            address=address,
            zip_code=zip_code,
            city=city
        )

    @classmethod
    def populate_database(cls, amount: int) -> None:
        full_names = FakeData.generate_full_names(amount)
        companies = FakeData.generate_companies(amount)
        locations = FakeData.generate_locations(amount * 2)
        phone_numbers = FakeData.generate_phone_numbers(amount * 2)

        corporate_customers = []
        private_customers = []

        for company in companies:
            location = locations.pop()
            client = {
                "customer_name": company.capitalize(),
                "phone": phone_numbers.pop(),
                "email": FakeData.generate_email("contact", company.lower()),
                "address": location.address,
                "zip_code": str(location.zip_code),
                "city": location.city
            }
            corporate_customers.append(client)

        for full_name in full_names:
            location = locations.pop()
            first_name, last_name = full_name.split(" ")
            client = {
                "contact_first_name": first_name,
                "contact_last_name": last_name,
                "phone": phone_numbers.pop(),
                "email": FakeData.generate_email(f"{first_name}.{last_name}"),
                "address": location.address,
                "zip_code": str(location.zip_code),
                "city": location.city
            }
            private_customers.append(client)

        for _ in range(amount):
            if randint(0, 1) % 2 == 0:
                cls.generate_corporate_customer(**corporate_customers.pop())
            else:
                cls.generate_private_customer(**private_customers.pop())

        corporates_created = amount - len(corporate_customers)
        privates_created = amount - len(private_customers)
        print(f"----- {corporates_created} Corporate and {privates_created} Private Customers generated -----")


def main():
    CustomerGenerator.populate_database(amount=100)


if __name__ == "__main__":
    main()
