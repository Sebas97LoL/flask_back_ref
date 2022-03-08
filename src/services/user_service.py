from src.repository.user_repository import UserRepository
from src.services.schema import UserSchema
from src.models.model import User


class UserService:

    def __init__(self):
        self.repository = UserRepository()

    def add_user(self, data):
        user = User(username=data['username'])
        print(user)
        schema = UserSchema()
        return schema.dump(data)
