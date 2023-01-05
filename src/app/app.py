from flask import Flask
from src.config import settings
from src import config
from src import database
from src.api import routes


def create_app():
    app = Flask(__name__)
    config.init(app)
    database.init()
    routes.init_app(app)

    @app.route("/")
    def home():
        return {"Hello": settings.MESSAGE}

    return app
