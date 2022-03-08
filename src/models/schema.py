from src.extensions import marshmallow


class RoleSchema(marshmallow.Schema):
    id = marshmallow.String(dump_only=True)
    name = marshmallow.String(dump_only=True)


class UserSchema(marshmallow.Schema):
    username = marshmallow.String(dump_only=True)
    email = marshmallow.String(dump_only=True)
    password = marshmallow.String(dumb_only=True)
    role = marshmallow.Integer(dumb_only=True)