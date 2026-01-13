from app.formatter.email_formatter import EmailFormatter
from app.formatter.telegram_formatter import TelegramFormatter
from app.formatter.discord_formatter import DiscordFormatter

def get_formatter(channel: str):
    if channel == "email":
        return EmailFormatter()
    elif channel == "telegram":
        return TelegramFormatter()
    elif channel == "discord":
        return DiscordFormatter()
    else:
        raise ValueError("Unsupported delivery channel")
