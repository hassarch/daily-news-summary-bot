from app.formatter.base import BaseFormatter

class TelegramFormatter(BaseFormatter):
    def format(self, data: dict) -> str:
        return (
            f"📰 *Daily News Digest*\n\n"
            f"*Title:* {data['title']}\n"
            f"*Source:* {data['source']}\n\n"
            f"📌 *Summary*\n"
            f"{data['summary']}\n\n"
            f"🔗 [Read more]({data['url']})"
        )
