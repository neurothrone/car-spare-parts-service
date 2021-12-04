"""
Config classes and logic for reading environment variables
for mongo and mysql databases.

Create two files in the same directory as this file 'config.py' and name them:
.env.mongo
.env.mysql

Write down these variables in the files and replace ... with the corresponding values:
DB_NAME=...
DB_PROTOCOL=...
DB_USER=...
DB_PASS=...
HOST=...
PORT=...
"""

from abc import ABC, abstractmethod

from dotenv import dotenv_values


class Config(ABC):
    _data: dict

    DB_NAME: str
    DB_PROTOCOL: str
    DB_USER: str
    DB_PASS: str
    HOST: str
    PORT: str

    @classmethod
    def read_env_values(cls) -> None:
        cls.DB_NAME: str = cls._data.get("DB_NAME", None)
        cls.DB_PROTOCOL: str = cls._data.get("DB_PROTOCOL", None)
        cls.DB_USER: str = cls._data.get("DB_USER", None)
        cls.DB_PASS: str = cls._data.get("DB_PASS", None)
        cls.HOST: str = cls._data.get("HOST", None)
        cls.PORT: str = cls._data.get("PORT", None)

    @abstractmethod
    def base_config(self) -> str:
        pass

    @abstractmethod
    def test_config(self) -> str:
        pass


class MongoConfig(Config):
    _data = {**dotenv_values(".env.mongo")}

    @classmethod
    def base_config(cls) -> str:
        cls.read_env_values()
        return f"{cls.DB_PROTOCOL}://{cls.DB_USER}:{cls.DB_PASS}@{cls.HOST}:{cls.PORT}"

    @classmethod
    def test_config(cls) -> str:
        raise NotImplementedError("test_config() is not implemented.")


class MysqlConfig(Config):
    _data = {**dotenv_values(".env.mysql")}

    @classmethod
    def base_config(cls) -> str:
        cls.read_env_values()
        return f"{cls.DB_PROTOCOL}://{cls.DB_USER}:{cls.DB_PASS}@{cls.HOST}:{cls.PORT}/{cls.DB_NAME}"

    @classmethod
    def test_config(cls) -> str:
        raise NotImplementedError("test_config() is not implemented.")


def main():
    print(MongoConfig.base_config())
    print(MongoConfig.DB_NAME)
    print(MysqlConfig.base_config())


if __name__ == "__main__":
    main()
