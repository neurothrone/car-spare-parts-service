from __future__ import annotations
from typing import Optional
from app.controllers.order_controller import OrderController
from generators.fake_data import FakeData
from app.controllers.customer_controller import CustomerController
from shared.validators import validate_length
from datetime import datetime
from datetime import date


class OrderGenerator:
    STATUS_LEN = 15

    @classmethod
    def generate(cls, order_date: date, shipped_date: date,
                 delivery_date: date, status: str, customer_id: Optional[int] = None) -> None:
        validate_length(provided=status, limit=OrderGenerator.STATUS_LEN)

        OrderController.create(order_date, shipped_date=shipped_date,
                               delivery_date=delivery_date, status=status, customer_id=customer_id)

    @classmethod
    def populate_database(cls, amount: int) -> None:
        order_dates = FakeData.generates_dates(amount)
        shipped_dates = FakeData.generates_dates(amount)
        delivery_dates = FakeData.generates_dates(amount)
        statuses = FakeData.generate_product_name()
        customers_id = CustomerController.find_all()[:amount]

        for order_date, shipped_date, delivery_date in zip(order_dates, shipped_dates, delivery_dates):
            cls.generate(order_date, shipped_date, delivery_date, statuses, customers_id)

        print(f"----- {amount} orders generated -----")


def main():

    OrderGenerator.populate_database(10)


if __name__ == "__main__":
    main()
