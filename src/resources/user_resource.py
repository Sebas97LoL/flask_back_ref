from flask import request
from flask_restful import Resource
from src.services.user_service import UserService


class UserResource(Resource):

    def get(self):
        service = UserService()
        response = service.add_user()
        schema = ""
        return ""

    def post(self):
        data = request.json
        service = UserService()
        response = service.add_user(data)
        return response

    def put(self):
        pass

    def delete(self):
        pass


class UsersResource(Resource):
    pass