import feedparser
import requests
from bs4 import BeautifulSoup

def fetch_rss(feed_url: str):
    feed = feedparser.parse(feed_url)
    articles = []

    for entry in feed.entries:
        try:
            url = entry.link
            response = requests.get(url, timeout=10)

            soup = BeautifulSoup(response.text, "html.parser")
            paragraphs = soup.find_all("p")
            content = " ".join([p.get_text() for p in paragraphs[:10]])

            article = {
                "title": entry.title,
                "source": feed.feed.get("title", "Unknown"),
                "url": url,
                "content": content,
                "published_at": entry.get("published", "")
            }

            articles.append(article)

        except Exception as e:
            print(f"RSS fetch error: {e}")

    return articles
