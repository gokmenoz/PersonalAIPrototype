import requests
from src.constants import SPORTS_API_URL

def handle_sports(query: str) -> str:
    try:
        response = requests.post(
            SPORTS_API_URL,
            json={"query": query},
            headers={"Content-Type": "application/json"},
            timeout=10,
        )
        if response.ok:
            return response.text.strip() or "🤖 (Empty response)"
        return f"⚠️ Travel API error: {response.status_code}"
    except Exception as e:
        return f"❌ Could not reach sports chatbot: {e}"