from fastapi import FastAPI
from app.fetcher.news_fetcher import fetch_all_news
from app.processor.preprocessor import preprocess_article
from app.summarizer.summarizer import summarize_article
from app.formatter.formatter_factory import get_formatter
from fastapi.responses import HTMLResponse
from app.delivery.sender_factory import get_sender
from apscheduler.schedulers.background import BackgroundScheduler
from app.scheduler.daily_job import run_daily_news_job


app = FastAPI(
    title="Daily News Summarizer Bot",
    description="AI-powered automated news summarization and delivery system",
    version="1.0.0"
)

@app.get("/")
def health_check():
    return {"status": "running"}

@app.get("/news")
def get_news():
    return fetch_all_news()




@app.get("/news/processed")
def get_processed_news():
    articles = fetch_all_news()
    return [preprocess_article(a) for a in articles[:5]]

@app.get("/news/summary")
def get_news_summary():
    articles = fetch_all_news()
    processed = preprocess_article(articles[0])
    return summarize_article(processed)


@app.get("/news/summary/{channel}")
def get_formatted_summary(channel: str):
    articles = fetch_all_news()
    processed = preprocess_article(articles[0])
    summary = summarize_article(processed)

    formatter = get_formatter(channel)
    return {
        "channel": channel,
        "formatted": formatter.format(summary)
    }


@app.get("/news/summary/email", response_class=HTMLResponse)
def get_email_preview():
    articles = fetch_all_news()
    processed = preprocess_article(articles[0])
    summary = summarize_article(processed)

    formatter = get_formatter("email")
    return formatter.format(summary)


@app.get("/news/send/{channel}")
def send_news(channel: str):
    articles = fetch_all_news()
    processed = preprocess_article(articles[0])
    summary = summarize_article(processed)

    formatter = get_formatter(channel)
    formatted = formatter.format(summary)

    sender = get_sender(channel)
    sender.send(formatted)

    return {"status": "sent", "channel": channel}


scheduler = BackgroundScheduler()

@app.on_event("startup")
def start_scheduler():
    scheduler.add_job(
        run_daily_news_job,
        trigger="cron",
        hour=9,
        minute=1
    )
    scheduler.start()
