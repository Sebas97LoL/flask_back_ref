from flask import request
from flask_restful import Resource
from src.services.role_service import RoleService


class RoleResource(Resource):

    def get(self):
        return RoleService().get_all()

    def post(self):
        data = request.json
        service = RoleService()
        return service.add_role(data)
