from app.delivery.email_sender import EmailSender
from app.delivery.telegram_sender import TelegramSender
from app.delivery.discord_sender import DiscordSender


def get_sender(channel: str):
    if channel == "email":
        return EmailSender()
    elif channel == "telegram":
        return TelegramSender()
    elif channel == "discord":
        return DiscordSender()
    else:
        raise ValueError("Unsupported delivery channel")
