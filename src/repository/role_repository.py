from src.models.model import Role
from src.exceptions.custom_exception import CustomException
from src.exceptions.base_response import ErrorResponse
from src.repository.abstract_repository import AbstractRepository
from src.exceptions.constants.model.role import error_messages
from src.exceptions.constants.http_statuses import BAD_REQUEST_STATUS


class RoleRepository(AbstractRepository):

    def __init__(self):
        super().__init__(Role)

    def add(self, instance):
        try:
            return super().add(instance)
        except Exception as e:
            self.session.close_session()
            response = ErrorResponse(
                message=error_messages['EN']['integrity_error'].format(instance.name),
                status_code=BAD_REQUEST_STATUS
            )
            raise CustomException(response)
