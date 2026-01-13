from app.formatter.base import BaseFormatter

class DiscordFormatter(BaseFormatter):
    def format(self, data: dict) -> str:
        return (
            f"📰 **{data['title']}**\n"
            f"**Source:** {data['source']}\n\n"
            f"{data['summary']}\n\n"
            f"🔗 {data['url']}"
        )
