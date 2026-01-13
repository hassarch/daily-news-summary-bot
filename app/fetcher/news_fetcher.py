from app.fetcher.rss_fetcher import fetch_rss
from app.fetcher.api_fetcher import fetch_news_api
from app.fetcher.deduplicator import deduplicate_articles

def fetch_all_news():
    rss_sources = [
        "https://feeds.bbci.co.uk/news/rss.xml",
        "https://rss.cnn.com/rss/edition.rss"
    ]

    articles = []

    for rss in rss_sources:
        articles.extend(fetch_rss(rss))

    articles.extend(fetch_news_api())

    return deduplicate_articles(articles)
