import requests
from app.delivery.base import BaseSender
from app.config import settings


class TelegramSender(BaseSender):
    def send(self, content: str):
        url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"

        payload = {
            "chat_id": settings.TELEGRAM_CHAT_ID,
            "text": content,
            "parse_mode": "Markdown"
        }

        requests.post(url, json=payload)
