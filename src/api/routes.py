from flask_restful import Api
from .messages import CustomerMessage, AttendantMessage
from flask import Blueprint

bp = Blueprint("routes", __name__)
api = Api(bp)


def init_router(app):
    api.add_resource(CustomerMessage, "/sms")
    api.add_resource(AttendantMessage, "/send")
    app.register_blueprint(bp)
