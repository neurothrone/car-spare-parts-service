import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    DB_NAME = os.getenv("DB_NAME")
    DB_PROTOCOL = os.getenv("DB_PROTOCOL")
    DB_USER = os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASS")
    HOST = os.getenv("HOST")
    PORT = os.getenv("PORT")

    @classmethod
    def get_base_config(cls) -> str:
        return f"{cls.DB_PROTOCOL}://{cls.DB_USER}:{cls.DB_PASS}@{cls.HOST}:{cls.PORT}/{cls.DB_NAME}"
