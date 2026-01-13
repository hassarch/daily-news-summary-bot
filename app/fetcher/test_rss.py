from rss_fetcher import fetch_rss

if __name__ == "__main__":
    articles = fetch_rss("https://feeds.bbci.co.uk/news/rss.xml")
    print(articles[0])
