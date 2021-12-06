from __future__ import annotations
from abc import ABC
from typing import Generic, Optional

import bson.errors
from bson import ObjectId

from app.data._mongo.models import ResultList, TBaseDocument


class BaseRepository(ABC):
    model: Generic[TBaseDocument] = None

    @classmethod
    def create(cls, **kwargs) -> None:
        obj = cls.model(**kwargs)
        obj.save()

    @classmethod
    def create_many(cls, data: list[dict]) -> int:
        insertions = cls.model.collection.insert_many(data)
        return len(insertions.inserted_ids)

    @classmethod
    def find(cls, many: bool = False,
             **kwargs) -> Optional[TBaseDocument | list[TBaseDocument]]:
        result = ResultList(cls.model(**item) for item in
                            cls.model.collection.find(kwargs))
        if many:
            return result
        return result.first_or_none()

    @classmethod
    def find_by_id(cls, _id: str) -> Optional[TBaseDocument]:
        try:
            return cls.find(_id=ObjectId(_id))
        except bson.errors.InvalidId:
            print(f"Error (bson.errors.InvalidId): That is not a valid "
                  f"ObjectId in function -> {cls.find_by_id.__name__}() "
                  f"on class -> {cls.__name__}.")

    @classmethod
    def find_all(cls, **kwargs) -> Optional[list[TBaseDocument]]:
        return cls.find(many=True, **kwargs)

    @classmethod
    def find_all_sort_by(cls, attribute: str, ascending: bool = True,
                         limit: Optional[int] = None) -> Optional[TBaseDocument | list[TBaseDocument]]:
        sort_in = 1 if ascending else -1
        if limit:
            return ResultList(cls.model(**item) for item in
                              cls.model.collection.find().sort(attribute, sort_in).limit())
        return ResultList(cls.model(**item) for item in
                          cls.model.collection.find().sort(attribute, sort_in))

    @classmethod
    def delete_by(cls, query: Optional[dict] = None, many: bool = True) -> int:
        if many:
            result = cls.model.collection.delete_many(query if query else {})
        else:
            result = cls.model.collection.delete_one(query if query else {})
        return result.deleted_count

    @classmethod
    def delete_by_regex(cls, attribute: str, regex: str, many: bool = True) -> int:
        query = {attribute: {"$regex": regex}}
        return cls.delete_by(query, many)

    @classmethod
    def delete_all(cls) -> int:
        return cls.delete_by()
