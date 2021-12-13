from app.settings import Settings

Settings.TESTING = True

from app.data._mongo.repositories.contact_person_repository import ContactPersonRepository as MongoContactPersonRepository
from app.data._mysql.repositories.contact_person_repository import ContactPersonRepository as MysqlContactPersonRepository


# class SupplierConverter:
#     @classmethod
def convert_from_mysql_to_mongo():
    for contact_person in MysqlContactPersonRepository.find_all():
        as_dict = contact_person.__dict__
        del as_dict["_sa_instance_state"]
        print()
        MongoContactPersonRepository.create(**as_dict)


def main():
    convert_from_mysql_to_mongo()


if __name__ == "__main__":
    main()
