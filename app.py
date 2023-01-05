from flask import Flask
from views import perform_query_blueprint


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(perform_query_blueprint)
    return app
