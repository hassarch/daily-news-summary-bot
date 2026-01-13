from app.processor.cleaner import clean_html
from app.processor.extractor import extract_main_content
from app.processor.language import detect_language

def preprocess_article(article: dict) -> dict:
    """
    Input: article from fetcher
    Output: cleaned, AI-ready article
    """

    url = article.get("url", "")
    raw_content = article.get("content", "")

    # Prefer full article extraction
    main_content = extract_main_content(url)

    # Fallback if extractor fails
    if not main_content:
        main_content = clean_html(raw_content)

    language = detect_language(main_content)

    return {
        **article,
        "content": main_content,
        "language": language
    }
