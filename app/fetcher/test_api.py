from api_fetcher import fetch_news_api

if __name__ == "__main__":
    articles = fetch_news_api()
    print(articles[0])
