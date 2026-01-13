import requests
from app.delivery.base import BaseSender
from app.config import settings


class DiscordSender(BaseSender):
    def send(self, content: str):
        payload = {
            "content": content
        }

        requests.post(settings.DISCORD_WEBHOOK_URL, json=payload)
