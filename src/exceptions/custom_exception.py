

class CustomException(Exception):
    def __init__(self, response):
        super().__init__()
        self.response = response
