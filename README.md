# 📰 Daily News Summarizer Bot

An AI-powered automated news aggregation and summarization system that fetches news from multiple sources, processes and summarizes them using Ollama (local LLMs), and delivers daily digests via email, Telegram, or Discord.

## ✨ Features

- **Multi-Source News Aggregation**: Fetches news from RSS feeds (BBC, CNN) and News API
- **AI-Powered Summarization**: Uses LangChain and Ollama to generate concise summaries locally
- **Smart Deduplication**: Removes duplicate articles across sources
- **Multi-Channel Delivery**: Supports Email, Telegram, and Discord
- **Automated Scheduling**: Daily news digest delivered at 9:01 AM
- **REST API**: FastAPI endpoints for testing and manual triggers
- **Content Processing**: Cleans, extracts, and preprocesses articles

## 🏗️ Architecture

```
app/
├── fetcher/          # News aggregation (RSS, API)
├── processor/        # Content cleaning and extraction
├── summarizer/       # LLM-based summarization
├── formatter/        # Channel-specific formatting
├── delivery/         # Multi-channel delivery (Email, Telegram, Discord)
└── scheduler/        # Automated daily jobs
```

## 🚀 Quick Start

### Prerequisites

- Docker and Docker Compose installed
- News API key
- Email credentials (for email delivery)
- Optional: Telegram bot token or Discord webhook

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <project-directory>
```

2. Configure environment variables:
```bash
cp .env.example .env
```

Edit `.env` with your credentials:
```env
NEWS_API_KEY=your_news_api_key

# Email Configuration
EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
EMAIL_RECEIVER=recipient@gmail.com

# Optional: Telegram
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id

# Optional: Discord
DISCORD_WEBHOOK_URL=your_webhook_url
```

### Running with Docker (Recommended)

1. Start the application:
```bash
docker-compose up -d
```

2. Pull an Ollama model (first time only):
```bash
docker exec -it ollama ollama pull llama2
```

3. Access the API at `http://localhost:8000`

4. View logs:
```bash
docker-compose logs -f app
```

5. Stop the application:
```bash
docker-compose down
```

### Running without Docker

1. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install and start Ollama:
```bash
# Install Ollama from https://ollama.ai
# Pull a model (e.g., llama2, mistral)
ollama pull llama2
```

4. Start the FastAPI server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## 📡 API Endpoints

### Health Check
```
GET /
```
Returns service status

### Fetch Raw News
```
GET /news
```
Returns aggregated news from all sources

### Get Processed News
```
GET /news/processed
```
Returns preprocessed articles (first 5)

### Get Summary
```
GET /news/summary
```
Returns AI-generated summary of the first article

### Get Formatted Summary
```
GET /news/summary/{channel}
```
Returns formatted summary for specific channel (email, telegram, discord)

### Preview Email
```
GET /news/summary/email
```
Returns HTML preview of email format

### Send News
```
GET /news/send/{channel}
```
Sends formatted news to specified channel

## ⚙️ Configuration

### News Sources

Edit `app/fetcher/news_fetcher.py` to add/remove RSS feeds:
```python
rss_sources = [
    "https://feeds.bbci.co.uk/news/rss.xml",
    "https://rss.cnn.com/rss/edition.rss",
    # Add more RSS feeds here
]
```

### Schedule Time

Modify `app/main.py` to change delivery time:
```python
scheduler.add_job(
    run_daily_news_job,
    trigger="cron",
    hour=9,    # Change hour
    minute=1   # Change minute
)
```

### Delivery Channel

Edit `app/scheduler/daily_job.py` to set default channel:
```python
channel = "email"  # Options: email, telegram, discord
```

## 🔧 Components

### Fetcher
- **RSS Fetcher**: Parses RSS feeds using feedparser
- **API Fetcher**: Fetches from News API
- **Deduplicator**: Removes duplicate articles

### Processor
- **Cleaner**: Removes HTML tags and special characters
- **Extractor**: Extracts article content using newspaper3k
- **Language Detection**: Filters non-English content
- **Preprocessor**: Orchestrates cleaning pipeline

### Summarizer
- **LLM Integration**: Uses LangChain with Ollama (local models)
- **Chunker**: Handles long articles
- **Custom Prompts**: Optimized for news summarization

### Formatter
- **Email**: HTML formatting with styling
- **Telegram**: Markdown formatting
- **Discord**: Embed formatting

### Delivery
- **Email**: SMTP delivery via Gmail
- **Telegram**: Bot API integration
- **Discord**: Webhook integration

## 📦 Dependencies

- **FastAPI**: Web framework
- **LangChain**: LLM orchestration
- **Ollama**: Local AI model inference
- **feedparser**: RSS parsing
- **newspaper3k**: Article extraction
- **BeautifulSoup4**: HTML parsing
- **APScheduler**: Job scheduling
- **requests**: HTTP client

## 🛠️ Development

### Running Tests

```bash
# Test RSS fetcher
python -m app.fetcher.test_rss

# Test API fetcher
python -m app.fetcher.test_api

# Test formatter
python -m app.formatter.test_formatter

# Test preprocessor
python -m app.processor.test_preprocessor

# Test summarizer
python -m app.summarizer.test_summarizer
```

### Project Structure

```
.
├── app/
│   ├── config.py              # Configuration management
│   ├── main.py                # FastAPI application
│   ├── fetcher/               # News aggregation
│   ├── processor/             # Content processing
│   ├── summarizer/            # AI summarization
│   ├── formatter/             # Output formatting
│   ├── delivery/              # Multi-channel delivery
│   └── scheduler/             # Automated jobs
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables
└── README.md                  # This file
```

## 🔐 Security Notes

- Never commit `.env` file to version control
- Use app-specific passwords for Gmail (not your main password)
- Keep API keys secure and rotate them regularly
- Review Discord webhook permissions
- Ollama runs locally, ensuring your data stays private

## 📝 License

This project is provided as-is for educational and personal use.

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## 📧 Support

For questions or issues, please open an issue in the repository.

---

Built with ❤️ using FastAPI, LangChain, and Ollama
