import os
import requests
from src.constants import EVENTS_API_URL

def handle_events(query: str) -> str:
    try:
        response = requests.post(
            EVENTS_API_URL,
            json={"query": query},
            headers={"Content-Type": "application/json"},
            timeout=10,
        )
        if response.ok:
            return response.text.strip() or "🤖 (Empty response)"
        return f"⚠️ Events API error: {response.status_code}"
    except Exception as e:
        return f"❌ Could not reach events chatbot: {e}"