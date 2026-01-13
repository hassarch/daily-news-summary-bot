from newspaper import Article

def extract_main_content(url: str) -> str:
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        print(f"Extractor error: {e}")
        return ""
