from random import randint

from faker import Faker
# from faker.providers import address
from faker.providers import company
from faker.exceptions import UniquenessException


class Location:
    def __init__(self, address: str, street_no: int, zip_code: int, city: str) -> None:
        self.address = address
        self.street_no = street_no
        self.zip_code = zip_code
        self.city = city

    def __str__(self) -> str:
        pass

    def __repr__(self) -> str:
        pass


class FakeStoreGenerator:

    @staticmethod
    def generate_store():
        # store_type, o, p
        # phone
        # email
        # address
        # zip code
        # city

        pass


class FakeData:
    faker: Faker = Faker("sv_SE")

    @classmethod
    def configure_locale(cls, locale: str) -> None:
        cls.faker = Faker(locale=locale)

    @staticmethod
    def generate_random_number(min_: int, max_: int) -> int:
        return randint(min_, max_)

    @staticmethod
    def generate_full_names(amount: int, unique: bool = True) -> list[str]:
        faker = Faker("sv_SE")

        if unique:
            full_names_set = set()
            while len(full_names_set) < amount:
                full_names_set.add(faker.name())
            return list(full_names_set)

        return [faker.name() for _ in range(amount)]

    @staticmethod
    def generate_phone_number() -> str:
        # +64 7X XXX XX XX
        #      012345678
        phone = "+64 7"
        for i in range(11):
            if i in [1, 5, 8]:
                phone += " "
            else:
                phone += str(FakeData.generate_random_number(min_=0, max_=9))
        return phone

    @staticmethod
    def generate_phone_numbers(amount: int) -> list[str]:
        phones = set()
        while len(phones) < amount:
            phones.add(FakeData.generate_phone_number())
        return list(phones)

    @staticmethod
    def generate_email(username: str, domain_name: str = "example", domain: str = "se") -> str:
        return f"{username}@{domain_name}.{domain}"

    @staticmethod
    def generate_emails(full_names: list[str], amount: int,
                        domain_name: str = "example", domain: str = "se") -> list[str]:
        emails = list()
        if amount > len(full_names):
            raise ValueError("Amount needs to be equal to or less than the length of full_names.")
        for i in range(amount):
            first_name, last_name = full_names[i].split(" ")
            email = FakeData.generate_email(
                username=f"{first_name.lower()}.{last_name.lower()}",
                domain_name=domain_name,
                domain=domain
            )
            emails.append(email)
        return emails

    @classmethod
    def generate_location(cls) -> Location:
        lines = cls.faker.address().split("\n")
        address, street_no = lines[0].split(" ")
        zip_code, city = lines[1].split(" ")
        return Location(address=address, street_no=int(street_no), zip_code=int(zip_code), city=city)

    @classmethod
    def generate_locations(cls, amount: int) -> list[Location]:
        return [FakeData.generate_location() for _ in range(amount)]


def print_sequence(sequence: list) -> None:
    for item in sequence:
        print(item)


def main():
    FakeData.generate_address()

    full_names = FakeData.generate_full_names(500)
    print_sequence(full_names)

    # emails = FakePersonGenerator.generate_emails(full_names, 500)
    # print_sequence(emails)

    # phone_numbers = FakePersonGenerator.generate_phone_numbers(500)
    # print_sequence(phone_numbers)

    # print(FakePersonGenerator.generate_phone_number())


if __name__ == "__main__":
    main()
