from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from app.summarizer.prompts import SUMMARY_PROMPT
from app.summarizer.llm import get_llm
from app.summarizer.chunker import chunk_text


def summarize_article(article: dict) -> dict:
    content = article.get("content", "")
    chunks = chunk_text(content)

    llm = get_llm()
    prompt = PromptTemplate(
        template=SUMMARY_PROMPT,
        input_variables=["text"]
    )

    chain = prompt | llm | StrOutputParser()

    try:
        # Only one chunk for speed
        result = chain.invoke({"text": chunks[0]})
    except Exception as e:
        result = f"⚠️ Summary failed: {str(e)}"

    return {
        "title": article.get("title"),
        "source": article.get("source"),
        "url": article.get("url"),
        "summary": result
    }
