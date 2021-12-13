from __future__ import annotations
from abc import ABC
from typing import Generic, Optional, TypeVar

TBaseDocument = TypeVar("TBaseDocument", bound="BaseDocument")


class BaseDocument(ABC, Generic[TBaseDocument], dict):
    collection = None

    def __init__(self, **data) -> None:
        super().__init__(**data)

        if "_id" not in data:
            self._id = None
        self.__dict__.update(data)

    def __repr__(self) -> str:
        attributes = ", ".join(f"{k}={v}" for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({attributes})"

    def __str__(self) -> str:
        attributes = "\n".join(f"\t{k}: {v}" for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}:\n{attributes}"

    def save(self) -> None:
        if not self._id:
            del self.__dict__["_id"]
            self.collection.insert_one(self.__dict__)
        else:
            self.replace_one({"_id": self._id}, self.__dict__)

    @classmethod
    def replace_one(cls, query: dict, new_values: dict) -> None:
        cls.collection.replace_one(query, new_values)

    def delete_field(self, field: str) -> None:
        self.collection.update_one({"_id": self._id}, {"$unset": {field: ""}})

    @classmethod
    def delete_all(cls) -> None:
        cls.collection.delete_many({})


class ResultList(list[Generic[TBaseDocument]]):
    def first_or_none(self) -> Optional[Generic[TBaseDocument]]:
        return self[0] if len(self) > 0 else None

    def last_or_none(self) -> Optional[Generic[TBaseDocument]]:
        return self[-1] if len(self) > 0 else None
