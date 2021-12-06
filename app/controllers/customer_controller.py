from typing import Optional

from app.controllers import BaseController
from app.data.models.customer import Customer
from app.data.repositories.customer_repository import CustomerRepository


class CustomerController(BaseController):
    repository = CustomerRepository
    required_attributes = {
        "customer_type", "customer_name", "contact_first_name",
        "contact_last_name", "phone", "email", "address",
        "zip_code", "city", "employee_id"
    }

    @staticmethod
    def find_by_id(_id: int) -> Optional[Customer]:
        return CustomerRepository.find_by_id(_id)
