from pymongo import MongoClient

from app.config import MongoConfig
from app.settings import Settings

client = MongoClient(MongoConfig.base_config())

if Settings.TESTING:
    db = client[f"{MongoConfig.DB_NAME}-test"]
else:
    db = client[MongoConfig.DB_NAME]


def drop_collection(col_name: str):
    db.drop_collection(col_name)


def drop_mongo_db(db_name: str):
    if db_name in client.list_database_names():
        client.drop_database(db_name)
        print(f"DB deleted: {db_name}")
    else:
        print(f"DB does not exist: {db_name}")
