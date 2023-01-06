from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from src.config import settings

client = Client(settings.TWILIO_SID, settings.TWILIO_TOKEN)


class Bot:
    def __init__(self, username: str) -> None:
        self.username = username
        self.botnumber = settings.BOT_NUMBER

    def send_message(self, message=None, media_url=None) -> str:
        try:
            __message = client.messages.create(
                body=str(message),
                media_url=media_url,
                from_=f"whatsapp:+{self.botnumber}",
                to=f"whatsapp:+{self.username}",
            )
            print(__message.sid)
            return "message sent"

        except TwilioRestException as e:
            print(f"Oh no: {e}")
        return "an error occurred trying to send message"
