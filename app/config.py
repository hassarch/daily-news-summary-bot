from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    APP_NAME: str = "Daily News Summarizer"

    # 📰 News API
    NEWS_API_KEY: str

    # 📧 Email
    EMAIL_SENDER: str
    EMAIL_PASSWORD: str
    EMAIL_RECEIVER: str

    # 🤖 Telegram
    TELEGRAM_BOT_TOKEN: str | None = None
    TELEGRAM_CHAT_ID: str | None = None

    # 💬 Discord
    DISCORD_WEBHOOK_URL: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()
