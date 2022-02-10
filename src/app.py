from flask import Flask


def run_app():
    app = Flask(__name__)
    app.config.from_object('src.config')
    return app
