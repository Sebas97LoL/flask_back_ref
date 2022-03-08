from src.repository.role_repository import RoleRepository
from src.services.schema import RoleSchema
from src.models.model import Role


class RoleService:

    def __init__(self):
        self.repository = RoleRepository()

    def add_role(self, data):
        role = Role(name=data['role'])
        new_role = self.repository.add(role)
        print("hey role", new_role)
        schema = RoleSchema()
        return schema.dump(new_role)

    def get_all(self):
        schema = RoleSchema(many=True)
        return schema.dump(self.repository.find_all())
