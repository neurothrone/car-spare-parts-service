from __future__ import annotations
from typing import Optional

from app.controllers.employee_controller import EmployeeController
from generators.fake_data import FakeData
from shared.validators import validate_length


class EmployeeGenerator:
    FIRST_NAME_LEN = 45
    LAST_NAME_LEN = 45
    PHONE_MAX_LEN = 25
    EMAIL_MAX_LEN = 100

    @classmethod
    def generate(cls, first_name: str, last_name: str, phone: str, email: str,
                 store_id: Optional[int | str] = None) -> None:
        validate_length(first_name, cls.FIRST_NAME_LEN)
        validate_length(last_name, cls.LAST_NAME_LEN)
        validate_length(phone, cls.PHONE_MAX_LEN)
        validate_length(email, cls.EMAIL_MAX_LEN)

        EmployeeController.create(
            first_name=first_name, last_name=last_name, phone=phone,
            email=email, store_id=store_id)

    @classmethod
    def populate_database(cls, amount: int) -> None:
        full_names = FakeData.generate_full_names(amount)
        phone_numbers = FakeData.generate_phone_numbers(amount)

        for i in range(amount):
            first_name, last_name = full_names[i].split(" ")
            email = FakeData.generate_email(
                username=f"{first_name}.{last_name}",
                domain_name="store",
                domain="se")

            cls.generate(
                first_name=first_name,
                last_name=last_name,
                phone=phone_numbers[i],
                email=email.lower())

        print(f"----- {amount} Employees generated -----")


def main():
    EmployeeGenerator.populate_database(amount=100)


if __name__ == "__main__":
    main()
