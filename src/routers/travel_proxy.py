import requests
import json
from constants import TRAVEL_API_URL

def handle_travel(query: str) -> str:
    try:
        response = requests.post(
            TRAVEL_API_URL,
            json={"message": query},
            headers={"Content-Type": "application/json"},
            timeout=30,
        )
        if response.ok:
            try:
                data = response.json()
                if "response" in data:
                    return data["response"]
                return response.text.strip() or "🤖 (Empty response)"
            except json.JSONDecodeError:
                return response.text.strip() or "🤖 (Empty response)"
        return f"⚠️ Travel API error: {response.status_code}"
    except Exception as e:
        return f"❌ Could not reach travel chatbot: {e}"