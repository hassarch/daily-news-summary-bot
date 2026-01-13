from app.formatter.formatter_factory import get_formatter

sample_data = {
    "title": "AI is changing the world",
    "source": "Tech News",
    "url": "https://example.com",
    "summary": "Headline:\nAI Boom\n\nSummary:\nAI is transforming industries.\n\nKey Points:\n- Growth\n- Innovation"
}

if __name__ == "__main__":
    formatter = get_formatter("telegram")
    print(formatter.format(sample_data))
