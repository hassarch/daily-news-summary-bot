import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.delivery.base import BaseSender
from app.config import settings


class EmailSender(BaseSender):
    def send(self, content: str):
        msg = MIMEMultipart("alternative")
        msg["Subject"] = "📰 Daily News Digest"
        msg["From"] = settings.EMAIL_SENDER
        msg["To"] = settings.EMAIL_RECEIVER

        msg.attach(MIMEText(content, "html"))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(settings.EMAIL_SENDER, settings.EMAIL_PASSWORD)
            server.send_message(msg)
