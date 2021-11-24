from typing import Type, TypeVar

from app.data._mysql.db import session
from app.data.models import BaseModel

T = TypeVar("T", bound=BaseModel)


class BaseRepository:
    @staticmethod
    def create(model: Type[T], **kwargs) -> T:
        instance = model(**kwargs)
        BaseRepository.save_to_db(instance)
        return instance

    @staticmethod
    def save_to_db(obj: Type[T]) -> None:
        session.add(obj)
        session.commit()

    @staticmethod
    def delete_from_db(obj: Type[T]) -> None:
        session.delete(obj)
        session.commit()

    @staticmethod
    def delete_all(model: Type[T]) -> None:
        session.query(model).delete()
        session.commit()

    @staticmethod
    def find_all(model: Type[T]) -> list[T]:
        return session.query(model).all()

    @staticmethod
    def all_to_dict(model: Type[T], items: list[T] = None) -> list[dict]:
        return [item.to_dict() for item in (items if items else model.find_all())]
