from abc import ABC
from typing import Optional

from app.data._mysql.db import session
from app.data._mysql.models import TBaseModel


class BaseRepository(ABC):
    model = None

    @classmethod
    def create(cls, **kwargs) -> None:
        instance = cls.model(**kwargs)
        cls.save_to_db(instance)

    @staticmethod
    def save_to_db(obj: TBaseModel) -> None:
        session.add(obj)
        session.commit()

    @staticmethod
    def delete_from_db(obj: TBaseModel) -> None:
        session.delete(obj)
        session.commit()

    @classmethod
    def delete_all(cls) -> int:
        deleted_count = session.query(cls.model).delete()
        session.commit()
        return deleted_count

    @classmethod
    def find_all(cls) -> Optional[list[TBaseModel]]:
        return session.query(cls.model).all()

    @classmethod
    def all_to_dict(cls, items: list[TBaseModel] = None) -> Optional[list[dict]]:
        return [item.to_dict() for item in (items if items else cls.model.find_all())]
