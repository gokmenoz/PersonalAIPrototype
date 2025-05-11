import requests
import json
from constants import NEWS_API_URL

def handle_news(query: str) -> str:
    try:
        response = requests.post(
            NEWS_API_URL,
            json={"message": query},
            headers={"Content-Type": "application/json"},
            timeout=30,
        )
        if response.ok:
            try:
                data = response.json()
                if "response" in data:
                    return data["response"]
                return response.text.strip() or "🤖 (No news found)"
            except json.JSONDecodeError:
                return response.text.strip() or "🤖 (No news found)"
        return f"⚠️ News API error: {response.status_code}"
    except Exception as e:
        return f"❌ Could not reach News chatbot: {e}"
