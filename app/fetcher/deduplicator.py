def deduplicate_articles(articles):
    seen_urls = set()
    unique_articles = []

    for article in articles:
        if article["url"] not in seen_urls:
            seen_urls.add(article["url"])
            unique_articles.append(article)

    return unique_articles
