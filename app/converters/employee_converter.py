from app.settings import Settings

Settings.TESTING = True

from app.data._mongo.repositories.employee_repository import EmployeeRepository as MongoEmployeeRepository
from app.data._mongo.repositories.store_repository import StoreRepository as MongoStoreRepository
from app.data._mysql.repositories.employee_repository import EmployeeRepository as MysqlEmployeeRepository


class EmployeeConverter:
    @classmethod
    def convert_from_mysql_to_mongo(cls):
        for employee in MysqlEmployeeRepository.find_all():
            as_dict = employee.__dict__

            as_dict = {key: value for key, value in as_dict.items() if value}
            del as_dict["_sa_instance_state"]

            MongoEmployeeRepository.create(**as_dict)

    @classmethod
    def delete_remnants(cls):
        for employee in MongoEmployeeRepository.find_all():
            employee_as_dict = employee.__dict__

            if employee_as_dict.get("employee_id", None):
                del employee_as_dict["employee_id"]

                if employee_as_dict.get("store_id", None):
                    store = MongoStoreRepository.find(store_id=employee_as_dict["store_id"])
                    employee_as_dict["store_id"] = store._id
                employee.replace_one({"_id": employee._id}, employee_as_dict)
