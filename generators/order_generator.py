from __future__ import annotations
from datetime import datetime
from typing import Optional

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
    def generate(cls, ordered_date: datetime, shipped_date: Optional[datetime],
                 delivery_date: datetime.date, status: str, customer_id: int) -> None:
        validate_length(provided=status, limit=OrderGenerator.STATUS_LEN)

        OrderController.create(ordered_date=ordered_date, shipped_date=shipped_date,
                               delivery_date=delivery_date, status=status, customer_id=customer_id)

    @classmethod
    def populate_database(cls, amount: int) -> None:
        CustomerGenerator.populate_database(amount)

        ordered_dates = FakeData.generate_datetimes(amount)
        customers = CustomerController.find_all()

        for ordered_date, customer in zip(
                ordered_dates,
                customers):
            cls.generate(ordered_date,
                         None,
                         None,
                         "Processing",
                         customer.customer_id)

        print(f"----- {amount} orders generated -----")


def main():
    OrderGenerator.populate_database(10)


if __name__ == "__main__":
    main()
