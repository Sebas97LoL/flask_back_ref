from src.exceptions.base_response import BaseResponse


class CustomException(Exception):
    def __init__(self, response: BaseResponse):
        super().__init__()
        self.response = response
