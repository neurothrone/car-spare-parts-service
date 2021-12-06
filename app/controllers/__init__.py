from abc import ABC
from pprint import pprint

from app.settings import Database, Settings

if Settings.DATABASE == Database.MONGO:
    from app.data._mongo.repositories import BaseRepository
else:
    from app.data._mysql.repositories import BaseRepository


class BaseController(ABC):
    repository = None
    required_attributes = {}

    @classmethod
    def validate(cls, store_data: dict) -> None:
        for attribute in cls.required_attributes:
            if attribute not in store_data:
                raise ValueError(f"Missing data when calling "
                                 f"{cls.validate.__name__}() "
                                 f"function on {cls.__name__}.")

    @classmethod
    def create(cls, **kwargs) -> None:
        cls.repository.create(**kwargs)

    @classmethod
    def find_all(cls) -> list:
        return cls.repository.find_all()

    @classmethod
    def delete_all(cls) -> int:
        return cls.repository.delete_all()

    @classmethod
    def all_to_dict(cls, items: list = None) -> list[dict]:
        return [item.to_dict() for item in (items if items else cls.find_all())]

    @staticmethod
    def pprint(obj) -> None:
        if not obj:
            return

        pprint(obj.to_dict(), sort_dicts=False)

    @classmethod
    def pprint_all(cls) -> None:
        pprint(cls.all_to_dict(), sort_dicts=False)
