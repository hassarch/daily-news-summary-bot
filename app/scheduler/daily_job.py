from app.fetcher.news_fetcher import fetch_all_news
from app.processor.preprocessor import preprocess_article
from app.summarizer.summarizer import summarize_article
from app.formatter.formatter_factory import get_formatter
from app.delivery.sender_factory import get_sender


def run_daily_news_job():
    print("🕒 Running daily TOP 3 news job...")

    articles = fetch_all_news()
    if not articles or len(articles) < 3:
        print("⚠️ Not enough articles found")
        return

    top_articles = articles[:3]
    summaries = []

    for idx, article in enumerate(top_articles, start=1):
        print(f"📰 Processing article {idx}")
        processed = preprocess_article(article)
        summary = summarize_article(processed)
        summaries.append(summary)

    # Combine all summaries into ONE digest
    combined_summary = {
        "title": "📰 Top 3 News Today",
        "source": "Multiple Sources",
        "url": "",
        "summary": ""
    }

    for i, s in enumerate(summaries, start=1):
        combined_summary["summary"] += (
            f"\n\n🔹 **{i}. {s['title']}**\n"
            f"{s['summary']}\n"
            f"🔗 {s['url']}\n"
        )

    # Choose channel
    channel = "email"  # or telegram / discord

    formatter = get_formatter(channel)
    formatted = formatter.format(combined_summary)

    sender = get_sender(channel)
    sender.send(formatted)

    print("✅ Top 3 daily news sent successfully")
