from flask import Blueprint
from flask_restful import Api
from src.resources.user_resource import UserResource

blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(blueprint)
api.add_resource(UserResource, "/user", endpoint="user")
