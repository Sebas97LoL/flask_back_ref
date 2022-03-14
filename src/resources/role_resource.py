from flask import request
from flask_restful import Resource, reqparse
from src.services.role_service import RoleService
from src.exceptions.custom_exception import CustomException


class RoleResource(Resource):

    def get(self, role_id):
        try:
            service = RoleService()
            response = service.find_by_id(role_id)
        except CustomException as e:
            return e.response.get_response()
        return response.get_response()

    def delete(self, role_id):
        service = RoleService()
        response = service.delete(role_id)
        return response.get_response()


class RolesResource(Resource):

    def get(self):
        return RoleService().find_all().get_response()

    def post(self):
        data = request.json
        try:
            service = RoleService()
            response = service.add_role(data)
        except CustomException as e:
            return e.response.get_response()
        return response.get_response()
