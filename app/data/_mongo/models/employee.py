from __future__ import annotations
from app.data._mongo.db import db
from app.data._mongo.models import BaseDocument


class Employee(BaseDocument):
    collection = db.employees
