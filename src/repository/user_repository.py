from src.models.model import User
from src.repository.abstract_repository import AbstractRepository


class UserRepository(AbstractRepository):

    def __init__(self):
        super().__init__(User)
