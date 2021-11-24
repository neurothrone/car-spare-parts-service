from pprint import pprint

from app.data.models import BaseModel, T
from app.data.repositories import BaseRepository


class BaseController:
    model = BaseModel

    @classmethod
    def create(cls, **kwargs) -> T:
        return BaseRepository.create(cls.model, **kwargs)

    @classmethod
    def find_all(cls) -> list[T]:
        return BaseRepository.find_all(cls.model)

    @classmethod
    def delete_all(cls) -> None:
        BaseRepository.delete_all(cls.model)

    @classmethod
    def all_to_dict(cls, items: list[T] = None) -> list[dict]:
        return [item.to_dict() for item in (items if items else cls.find_all())]

    @staticmethod
    def pprint(obj: T) -> None:
        pprint(obj.to_dict(), sort_dicts=False)

    @classmethod
    def pprint_all(cls) -> None:
        pprint(cls.all_to_dict(), sort_dicts=False)
