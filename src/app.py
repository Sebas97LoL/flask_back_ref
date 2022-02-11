from flask import Flask
from src.extensions import db, migrate
from src import routes


def run_app():
    app = Flask(__name__)
    app.config.from_object('src.config')

    configure_extensions(app)
    #register_blueprints(app)

    return app


def configure_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    app.register_blueprint(routes.blueprint)
