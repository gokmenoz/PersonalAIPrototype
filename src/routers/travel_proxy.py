import os
import requests

TRAVEL_API_URL = os.getenv("TRAVEL_API_URL", "http://localhost:8001/chat")

def handle_travel(query: str) -> str:
    try:
        response = requests.post(
            TRAVEL_API_URL,
            json={"query": query},
            headers={"Content-Type": "application/json"},
            timeout=10,
        )
        if response.ok:
            return response.text.strip() or "🤖 (Empty response)"
        return f"⚠️ Travel API error: {response.status_code}"
    except Exception as e:
        return f"❌ Could not reach travel chatbot: {e}"