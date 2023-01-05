from flask_restful import Resource, Api, request
from flask import Blueprint
import json
import requests
from src.api.bot import Bot

bp = Blueprint("routes", __name__)
api = Api(bp)


class MessageReceiver(Resource):
    def post(self):
        username = request.form.get("From").replace("whatsapp:+", "")
        bot = Bot(username=username)
        bot.send_message(message=f"Olá, {username}!")

        return {"success": "message received"}, 200


def init_app(app):
    api.add_resource(MessageReceiver, "/sms")

    app.register_blueprint(bp)
