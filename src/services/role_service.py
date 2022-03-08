from src.models.model import Role
from src.models.schema import RoleSchema
from src.repository.role_repository import RoleRepository
from src.exceptions.custom_exception import CustomException
from src.exceptions.base_response import SuccessResponse


class RoleService:

    def __init__(self):
        self.repository = RoleRepository()

    def add_role(self, data):
        role = Role(name=data['role'])
        try:
            new_role = self.repository.add(role)
            schema = RoleSchema()
            return SuccessResponse(schema.dump(new_role))
        except CustomException as e:
            raise e

    def find_by_id(self, instance_id):
        schema = RoleSchema()
        role = self.repository.find_by_id(instance_id)
        response = schema.dump(role)
        return SuccessResponse(response)

    def find_all(self):
        schema = RoleSchema(many=True)
        response = schema.dump(self.repository.find_all())
        return SuccessResponse(response)
