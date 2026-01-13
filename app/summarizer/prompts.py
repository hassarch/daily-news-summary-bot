SUMMARY_PROMPT = """
You are a professional news analyst.

Summarize the following news article clearly and factually.

Rules:
- No hallucinations
- No opinions
- Simple language
- Maximum 5 bullet points

Article:
{text}

Return in this format:

Headline:
<one short headline>

Summary:
<3–4 sentence paragraph>

Key Points:
- point 1
- point 2
- point 3
"""
