from abc import ABC
from src.repository.connection import Connection
from src.exceptions.custom_exception import CustomException
from src.exceptions.base_response import ErrorResponse
from src.exceptions.constants.http_statuses import BAD_REQUEST_STATUS
from src.exceptions.constants.model.error_messages import ENTITY_ID_NOT_IN_DATABASE_ERROR


class AbstractRepository(ABC):

    def __init__(self, model):
        self.model = model
        self.model_name = model.__name__
        self.session = Connection

    def add(self, instance):
        self.session.get_instance().add(instance)
        self.session.commit_changes()
        last_record_added = self.session.get_instance().query(self.model).order_by(self.model.id.desc()).first()
        self.session.close_session()
        return last_record_added

    def delete(self, instance):
        return self.session.get_instance().delete(instance)

    def find_by_id(self, instance_id):
        session = self.session.get_instance()
        data = session.query(self.model).get(instance_id,)
        if data:
            self.session.close_session()
            return data
        else:
            response = ErrorResponse(
                message=ENTITY_ID_NOT_IN_DATABASE_ERROR.format(self.model_name),
                status_code=BAD_REQUEST_STATUS
            )
            raise CustomException(response)

    def find_all(self):
        session = self.session.get_instance()
        data = session.query(self.model).all()
        self.session.close_session()
        return data

