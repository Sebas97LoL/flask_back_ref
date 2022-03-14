from flask import Blueprint
from flask_restful import Api
from src.resources.user_resource import UserResource, UsersResource
from src.resources.role_resource import RoleResource, RolesResource

blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(blueprint)

api.add_resource(UserResource, "/users/<string:username>", endpoint="user")
api.add_resource(UsersResource, "/users", endpoint="users")
api.add_resource(RoleResource, "/roles/<int:role_id>", endpoint="role")
api.add_resource(RolesResource, "/roles", endpoint="roles")
