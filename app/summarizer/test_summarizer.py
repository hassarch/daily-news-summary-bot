from app.fetcher.news_fetcher import fetch_all_news
from app.processor.preprocessor import preprocess_article
from app.summarizer.summarizer import summarize_article

if __name__ == "__main__":
    articles = fetch_all_news()
    processed = preprocess_article(articles[0])
    summary = summarize_article(processed)

    print(summary["summary"])
