from app.settings import Settings

Settings.TESTING = True

from app.data._mongo.repositories.employee_repository import EmployeeRepository as MongoEmployeeRepository
from app.data._mongo.repositories.store_repository import StoreRepository as MongoStoreRepository
from app.data._mysql.repositories.store_repository import StoreRepository as MysqlStoreRepository


class StoreConverter:
    @classmethod
    def convert_from_mysql_to_mongo(cls):
        for store in MysqlStoreRepository.find_all():
            as_dict = store.__dict__
            del as_dict["_sa_instance_state"]
            MongoStoreRepository.create(**as_dict)

    @classmethod
    def connect_employees_to_stores(cls):
        employees = [employee.__dict__ for employee in MongoEmployeeRepository.find_all()]

        for store in MongoStoreRepository.find_all():
            store_as_dict = store.__dict__

            if not store_as_dict.get("employees", None):
                store_as_dict["employees"] = []

            for employee in employees:
                if not employee.get("store_id", None):
                    continue

                if employee["store_id"] == store_as_dict["store_id"]:
                    del employee["employee_id"]
                    del employee["store_id"]
                    store_as_dict["employees"].append(employee)
                    store.replace_one({"_id": store_as_dict["_id"]}, store_as_dict)

    @classmethod
    def delete_remnants(cls):
        # delete store_id mysql remnant
        for store in MongoStoreRepository.find_all():
            store_as_dict = store.__dict__

            if store_as_dict.get("store_id", None):
                del store_as_dict["store_id"]
                store.replace_one({"_id": store._id}, store_as_dict)
