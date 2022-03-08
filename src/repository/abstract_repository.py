from abc import ABC
from src.repository.connection import Connection


class AbstractRepository(ABC):

    def __init__(self, model):
        self.model = model
        self.session = Connection

    def add(self, instance):
        try:
            print("hola")
            self.session.get_instance().add(instance)
            self.session.commit_changes()
            print("HEY")
            return instance
        except Exception as e:
            print("holiwii")
            self.session.close_session()
            return "add error" + e.__repr__()

    def find_all(self):
        session = self.session.get_instance()
        return session.query(self.model).all()

    def find_by_id(self, instance_id):
        session = self.session.get_instance()
        return session.query(self.model).get(instance_id)
