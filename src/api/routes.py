from flask_restful import Resource, Api, request
from flask import Blueprint
from src.api.bot import Bot

bp = Blueprint("routes", __name__)
api = Api(bp)


class MessageReceiver(Resource):
    def post(self):
        username = request.form.get("From").replace("whatsapp:+", "")
        bot = Bot(username=username)
        bot.send_message(
            message=f"Olá! Me diga o que deseja ou digite 'atendente' que uma pessoa do nosso time irá lhe ajudar!"
        )

        return {"username": f"{username}"}, 200


def init_app(app):
    api.add_resource(MessageReceiver, "/sms")

    app.register_blueprint(bp)
