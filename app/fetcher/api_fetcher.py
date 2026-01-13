import requests
from app.config import settings

NEWS_API_URL = "https://newsapi.org/v2/top-headlines"

def fetch_news_api(category="technology", country="us"):
    params = {
        "apiKey": settings.NEWS_API_KEY,
        "category": category,
        "country": country,
        "pageSize": 10
    }

    response = requests.get(NEWS_API_URL, params=params)
    data = response.json()

    articles = []

    for item in data.get("articles", []):
        article = {
            "title": item.get("title"),
            "source": item["source"]["name"],
            "url": item.get("url"),
            "content": item.get("content") or "",
            "published_at": item.get("publishedAt")
        }
        articles.append(article)

    return articles
