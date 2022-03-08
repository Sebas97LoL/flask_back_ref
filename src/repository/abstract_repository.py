from abc import ABC
from src.repository.connection import Connection


class AbstractRepository(ABC):

    def __init__(self, model):
        self.model = model
        self.session = Connection

    def add(self, instance):
        self.session.get_instance().add(instance)
        self.session.commit_changes()
        last_record_added = self.session.get_instance().query(self.model).order_by(self.model.id.desc()).first()
        return last_record_added

    def find_all(self):
        session = self.session.get_instance()
        return session.query(self.model).all()

    def find_by_id(self, instance_id):
        session = self.session.get_instance()
        return session.query(self.model).get(instance_id)
