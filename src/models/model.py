from sqlalchemy.ext.hybrid import hybrid_property
from ..extensions import db, pwd_context


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True, nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    _password = db.Column('password', db.String(255), nullable=False)
    active = db.Column(db.Boolean, default=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    role = db.relationship('Role')

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = pwd_context.hash(value)

    def __repr__(self):
        return "<User %s>" % self.username


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
