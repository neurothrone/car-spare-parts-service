import datetime
from random import randint

from faker import Faker


# from faker.providers import address
# from faker.providers import company
# from faker.exceptions import UniquenessException


class Location:
    def __init__(self, address: str, street_no: int, zip_code: int, city: str) -> None:
        self.address = address
        self.street_no = street_no
        self.zip_code = zip_code
        self.city = city

    def __repr__(self) -> str:
        return f"Location(address={self.address}, street_no={self.street_no}," \
               f" zip_code={self.zip_code}, city={self.city})"

    def __str__(self) -> str:
        return f"{self.address} {self.street_no}\n{self.zip_code} {self.city}"


class FakeData:
    _faker: Faker = Faker("sv_SE")

    MIN_AGE = 18
    MAX_AGE = 72

    @classmethod
    def configure_locale(cls, locale: str) -> None:
        cls._faker = Faker(locale=locale)

    @staticmethod
    def generate_random_number(min_: int, max_: int) -> int:
        return randint(min_, max_)

    @classmethod
    def generate_full_names(cls, amount: int, unique: bool = True) -> list[str]:
        if unique:
            full_names_set = set()
            while len(full_names_set) < amount:
                full_names_set.add(cls._faker.name())
            return list(full_names_set)

        return [cls._faker.name() for _ in range(amount)]

    @classmethod
    def generate_phone_number(cls) -> str:
        return cls._faker.phone_number()

    @staticmethod
    def generate_phone_numbers(amount: int) -> list[str]:
        phones = set()
        while len(phones) < amount:
            phones.add(FakeData.generate_phone_number())
        return list(phones)

    @staticmethod
    def generate_email(username: str, domain_name: str = "example", domain: str = "se") -> str:
        return f"{username}@{domain_name}.{domain}"

    @classmethod
    def generate_emails(cls, full_names: list[str], amount: int,
                        domain_name: str = "example", domain: str = "se") -> list[str]:
        emails = list()
        if amount > len(full_names):
            raise ValueError("Amount needs to be equal to or less than the length of full_names.")
        for i in range(amount):
            first_name, last_name = full_names[i].split(" ")
            email = cls.generate_email(
                username=f"{first_name.lower()}.{last_name.lower()}",
                domain_name=domain_name,
                domain=domain
            )
            emails.append(email)
        return emails

    @classmethod
    def generate_location(cls) -> Location:
        lines = cls._faker.address().split("\n")
        address, street_no = lines[0].split(" ")
        zip_code, city = lines[1].split(" ")
        return Location(address=address, street_no=int(street_no), zip_code=int(zip_code), city=city)

    @classmethod
    def generate_locations(cls, amount: int) -> list[Location]:
        return [cls.generate_location() for _ in range(amount)]

    @classmethod
    def generate_license_plate(cls) -> str:
        return cls._faker.license_plate()

    @classmethod
    def generate_license_plates(cls, amount: int) -> list[str]:
        license_plates = set()
        while len(license_plates) < amount:
            license_plates.add(FakeData.generate_license_plate())
        return list(license_plates)

    @classmethod
    def generate_color_name(cls) -> str:
        return cls._faker.safe_color_name()

    @classmethod
    def generate_15_color_names(cls) -> list[str]:
        max_colors = 15
        colors = set()
        while len(colors) < max_colors:
            colors.add(FakeData.generate_color_name())
        return list(colors)

    @classmethod
    def generate_date(cls) -> datetime.date:
        return cls._faker.date_of_birth(minimum_age=FakeData.MIN_AGE, maximum_age=FakeData.MAX_AGE)

    @classmethod
    def generates_dates(cls, amount: int) -> list[datetime.date]:
        return [cls.generate_date() for _ in range(amount)]

    @classmethod
    def generate_car(cls):
        pass

    @classmethod
    def generate_cars(cls):
        pass


def print_sequence(sequence: list) -> None:
    for item in sequence:
        print(item)


def test_name_generation():
    full_names = FakeData.generate_full_names(500)
    print_sequence(full_names)


def test_email_generation():
    full_names = FakeData.generate_full_names(500)
    emails = FakeData.generate_emails(full_names, 500)
    print_sequence(emails)


def test_phone_generation():
    phone_numbers = FakeData.generate_phone_numbers(500)
    print_sequence(phone_numbers)


def test_address_generation():
    locations = FakeData.generate_locations(500)
    print_sequence(locations)


def test_reg_no_generation():
    # print(FakeData.generate_license_plate())
    license_plates = FakeData.generate_license_plates(500)
    print_sequence(license_plates)


def test_color_generation():
    # print(FakeData.generate_color_name())
    print_sequence(FakeData.generate_15_color_names())


def test_date_generation():
    # print(FakeData.generate_date())
    print_sequence(FakeData.generates_dates(500))


def main():
    # test_name_generation()
    # test_email_generation()
    # test_phone_generation()
    # test_address_generation()
    # test_reg_no_generation()
    # test_color_generation()
    test_date_generation()


if __name__ == "__main__":
    main()
