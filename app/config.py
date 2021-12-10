"""
Config classes and logic for reading environment variables
for mongo and mysql databases.

1. Create a file directory in the root directory, same directory as the file .gitignore, and name it '.env'.
2. Write down these variables in the files:

MONGO_DB_NAME=...
MONGO_DB_PROTOCOL=...
MONGO_DB_USER=...
MONGO_DB_PASS=...
MONGO_DB_HOST=...
MONGO_DB_PORT=...

MYSQL_DB_NAME=...
MYSQL_DB_PROTOCOL=...
MYSQL_DB_USER=...
MYSQL_DB_PASS=...
MYSQL_DB_HOST=...
MYSQL_DB_PORT=...

3. Replace ... with corresponding values.
"""

from abc import ABC, abstractmethod
import os

from dotenv import load_dotenv

load_dotenv()


class Config(ABC):
    DB_NAME: str
    DB_PROTOCOL: str
    DB_USER: str
    DB_PASS: str
    HOST: str
    PORT: str

    @abstractmethod
    def read_env_values(self) -> None:
        pass

    @abstractmethod
    def base_config(self) -> str:
        pass

    @abstractmethod
    def test_config(self) -> str:
        pass


class MongoConfig(Config):
    @classmethod
    def read_env_values(cls) -> None:
        cls.DB_NAME = os.getenv("MONGO_DB_NAME", "DB_NAME")
        cls.DB_PROTOCOL = os.getenv("MONGO_DB_PROTOCOL", "DB_PROTOCOL")
        cls.DB_USER = os.getenv("MONGO_DB_USER", "DB_USER")
        cls.DB_PASS = os.getenv("MONGO_DB_PASS", "DB_PASS")
        cls.HOST = os.getenv("MONGO_DB_HOST", "HOST")
        cls.PORT = os.getenv("MONGO_DB_PORT", "PORT")

    @classmethod
    def base_config(cls) -> str:
        cls.read_env_values()
        return f"{cls.DB_PROTOCOL}://{cls.DB_USER}:{cls.DB_PASS}@{cls.HOST}:{cls.PORT}"

    @classmethod
    def test_config(cls) -> str:
        raise NotImplementedError("test_config() is not implemented.")


class MysqlConfig(Config):
    @classmethod
    def read_env_values(cls) -> None:
        cls.DB_NAME = os.getenv("MYSQL_DB_NAME", "DB_NAME")
        cls.DB_PROTOCOL = os.getenv("MYSQL_DB_PROTOCOL", "DB_PROTOCOL")
        cls.DB_USER = os.getenv("MYSQL_DB_USER", "DB_USER")
        cls.DB_PASS = os.getenv("MYSQL_DB_PASS", "DB_PASS")
        cls.HOST = os.getenv("MYSQL_DB_HOST", "HOST")
        cls.PORT = os.getenv("MYSQL_DB_PORT", "PORT")

    @classmethod
    def base_config(cls) -> str:
        cls.read_env_values()
        return f"{cls.DB_PROTOCOL}://{cls.DB_USER}:{cls.DB_PASS}@{cls.HOST}:{cls.PORT}/{cls.DB_NAME}"

    @classmethod
    def test_config(cls) -> str:
        return cls.base_config() + "-test"
