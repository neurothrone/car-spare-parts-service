from __future__ import annotations
from app.settings import Settings, Database

Settings.TESTING = True

from app.controllers.customer_controller import CustomerController
from app.controllers.order_controller import OrderController
from generators.customer_generator import CustomerGenerator
from shared.validators import validate_length
import random
import datetime
from faker import Faker


class OrderGenerator:
    STATUS_LEN = 15

    @classmethod
    def generate(cls, ordered_date: datetime, shipped_date: datetime,
                 delivery_date: datetime, status: str, customer_id: int) -> None:
        validate_length(provided=status, limit=OrderGenerator.STATUS_LEN)

        OrderController.create(ordered_date=ordered_date, shipped_date=shipped_date,
                               delivery_date=delivery_date, status=status, customer_id=customer_id)

    @classmethod
    def populate_database(cls, amount: int) -> None:
        CustomerGenerator.populate_database(amount)

        fake = Faker()
        start_date_ordered_dates = datetime.date(year=2021, month=1, day=1)
        end_date_ordered_dates = datetime.date(year=2021, month=1, day=15)

        start_date_shipped_dates = datetime.date(year=2021, month=1, day=15)
        end_date_shipped_dates = datetime.date(year=2021, month=1, day=30)

        start_date_delivery_dates = datetime.date(year=2021, month=1, day=30)
        end_date_delivery_dates = datetime.date(year=2021, month=3, day=30)

        for i in range(amount):
            if Settings.DATABASE == Database.MONGO:
                pass

            else:
                customer_id = random.choice(CustomerController.find_all()).customer_id

                ordered_dates = fake.date_between(start_date=start_date_ordered_dates, end_date=end_date_ordered_dates)
                shipped_dates = fake.date_between(start_date=start_date_shipped_dates, end_date=end_date_shipped_dates)
                delivery_dates = fake.date_between(start_date=start_date_delivery_dates,
                                                   end_date=end_date_delivery_dates)

                cls.generate(ordered_date=ordered_dates,
                             shipped_date=shipped_dates,
                             delivery_date=delivery_dates,
                             status="Processing",
                             customer_id=customer_id)

        print(f"----- {amount} orders generated -----")


def main():
    OrderGenerator.populate_database(10)


if __name__ == "__main__":
    main()
