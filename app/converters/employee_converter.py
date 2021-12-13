import pprint

from app.settings import Settings

Settings.TESTING = True

from app.data._mongo.repositories.employee_repository import EmployeeRepository as MongoEmployeeRepository
from app.data._mysql.repositories.employee_repository import EmployeeRepository as MysqlEmployeeRepository

# TODO: connect employees to stores
# TODO: add employees to stores OR save store_id in Employee model
# TODO: tests

class EmployeeConverter:
    @classmethod
    def convert_from_mysql_to_mongo(cls):
        for employee in MysqlEmployeeRepository.find_all():
            as_dict = employee.__dict__

            del as_dict["_sa_instance_state"]
            as_dict = {key: value for key, value in as_dict.items() if value}
            print()

            pprint.pprint(as_dict)
            # {'email': 'bernt.lindkvist@store.se',
            #  'employee_id': 1,
            #  'first_name': 'Bernt',
            #  'last_name': 'Lindkvist',
            #  'phone': '075-52 02 86'}
            quit()

            MongoEmployeeRepository.create(**as_dict)
