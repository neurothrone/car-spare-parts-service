from typing import Type, TypeVar

from app.data._mysql.db import session
from app.data.models import BaseModel

T = TypeVar("T", bound=BaseModel)


class BaseRepository:
    @staticmethod
    def create(model: Type[T], **kwargs) -> None:
        instance = model(**kwargs)
        BaseRepository.save_to_db(instance)

    @staticmethod
    def save_to_db(obj: T) -> None:
        session.add(obj)
        session.commit()

    @staticmethod
    def delete_from_db(obj: T) -> None:
        session.delete(obj)
        session.commit()

    @staticmethod
    def delete_all(model: T) -> None:
        session.query(model).delete()
        session.commit()

    @staticmethod
    def find_all(model: T) -> list[T]:
        return session.query(model).all()

    @staticmethod
    def all_to_dict(model: T, items: list[T] = None) -> list[dict]:
        return [item.to_dict() for item in (items if items else model.find_all())]
