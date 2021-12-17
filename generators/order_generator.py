from __future__ import annotations
import datetime
from random import choice

from app.settings import Settings

Settings.TESTING = True

from app.controllers.customer_controller import CustomerController
from app.controllers.order_controller import OrderController
from generators.customer_generator import CustomerGenerator
from generators.fake_data import FakeData
from shared.validators import validate_length


class OrderGenerator:
    STATUS_LEN = 15

    @classmethod
    def generate(cls, ordered_date: datetime, shipped_date: datetime,
                 delivery_date: datetime.date, status: str, customer_id: int) -> None:
        validate_length(provided=status, limit=OrderGenerator.STATUS_LEN)

        OrderController.create(ordered_date=ordered_date, shipped_date=shipped_date,
                               delivery_date=delivery_date, status=status, customer_id=customer_id)

    @classmethod
    def populate_database(cls, amount: int) -> None:
        CustomerGenerator.populate_database(amount)

        ordered_datetimes = FakeData.generate_datetimes(
            amount,
            start=datetime.date(year=2021, month=1, day=1),
            end=datetime.date(year=2021, month=1, day=15))
        shipped_datetimes = FakeData.generate_datetimes(
            amount,
            start=datetime.date(year=2021, month=1, day=15),
            end=datetime.date(year=2021, month=1, day=30))
        delivery_datetimes = FakeData.generate_datetimes(
            amount,
            start=datetime.date(year=2021, month=1, day=30),
            end=datetime.date(year=2021, month=3, day=30))
        customers = CustomerController.find_all()

        for ordered_datetime, shipped_datetime, delivery_date, customer in zip(
                ordered_datetimes, shipped_datetimes, delivery_datetimes, customers):

            if not shipped_datetime:
                status = "Processing"
            elif delivery_date.date() < datetime.datetime.today().date():
                status = "Delivered"
            elif shipped_datetime < delivery_date:
                status = "On delivery"
            else:
                status = "To be updated..."

            cls.generate(ordered_date=ordered_datetime,
                         shipped_date=shipped_datetime,
                         delivery_date=delivery_date.date(),
                         status=status,
                         customer_id=choice(customers).customer_id)

        print(f"----- {amount} orders generated -----")


def main():
    OrderGenerator.populate_database(10)


if __name__ == "__main__":
    main()
