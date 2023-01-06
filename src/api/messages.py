from flask_restful import Resource, request
import json
from src.api.bot import Bot
import logging


class CustomerMessage(Resource):
    def post(self):
        username = request.form.get("From").replace("whatsapp:+", "")
        message = request.form.get("Body")
        bot = Bot(username=username)
        bot.send_message(message=message)
        logging.info(message)

        return "OK", 200


class AttendantMessage(Resource):
    def post(self):
        data = json.loads(request.data)
        print(json.dumps(data, indent=2))

        return {"received": data["message"]}
