import requests
from src.constants import NEWS_API_URL

def handle_news(query: str) -> str:
    try:
        response = requests.post(
            NEWS_API_URL,
            json={"query": query},
            headers={"Content-Type": "application/json"},
            timeout=10,
        )
        if response.ok:
            return response.text.strip() or "🤖 (No news found)"
        return f"⚠️ News API error: {response.status_code}"
    except Exception as e:
        return f"❌ Could not reach News chatbot: {e}"
