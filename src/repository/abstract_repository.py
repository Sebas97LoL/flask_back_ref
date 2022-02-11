from abc import ABC
from typing import TypeVar
from .connection import Connection


class AbstractRepository(ABC):

    def __init__(self, model):
        self.model = model
        self.session = Connection.get_instance()

    def add(self, instance):
        self.session.add(instance)
        self.session.commit_changes()
        return instance

    def find_by_id(self, instance_id):
        instance = self.session.query(self.model).get(instance_id)
        return instance
