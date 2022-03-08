from src.models.model import Role
from src.repository.abstract_repository import AbstractRepository


class RoleRepository(AbstractRepository):

    def __init__(self):
        super().__init__(Role)
