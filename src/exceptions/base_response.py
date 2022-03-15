from abc import ABC, abstractmethod
from src.exceptions.constants.http_statuses import OK_STATUS


class BaseResponse(ABC):
    def __init__(self, status_code):
        self.status_code = status_code

    @abstractmethod
    def get_response(self):
        pass


class ErrorResponse(BaseResponse):
    def __init__(self, message, status_code):
        super().__init__(status_code)
        self.message = message

    def get_response(self):
        return {
            'body': {
                'message': self.message
            },
        }, self.status_code


class SuccessResponse(BaseResponse):
    def __init__(self, body):
        super().__init__(OK_STATUS)
        self.body = body

    def get_response(self):
        return {
            'body': self.body,
        }, self.status_code
