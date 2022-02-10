from flask import Blueprint
from flask_restful import Api
#from src.resources import

blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(blueprint)
api.add_resource(resources.UserResource, "/user", endpoint="user")
api.add_resource(resources.UsersResource, "/users", endpoint="users")
