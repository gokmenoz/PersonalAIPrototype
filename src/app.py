# app.py

import streamlit as st
from intent import detect_category_nova
from routers.travel_proxy import handle_travel
from routers.events_proxy import handle_events
from routers.news_proxy import handle_news
from routers.sports_proxy import handle_sports
# from routers.ai_proxy import handle_ai

st.set_page_config(page_title="🤖 Smart Chatbot", layout="centered")
st.title("💬 Personal AI Assistant")

query = st.text_input("Ask me anything:")

if st.button("Submit"):
    if not query.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Detecting intent..."):
            try:
                intent = detect_category_nova(query)
                st.write(f"🧠 Detected intent: `{intent}`")
            except Exception as e:
                st.error(f"❌ Failed to detect intent: {e}")
                st.stop()

        if intent == "travel":
            with st.spinner("Asking TravelBot..."):
                result = handle_travel(query)
                st.success("🌍 TravelBot says:")
                st.write(result)

        elif intent == "events":
            with st.spinner("Checking local events..."):
                result = handle_events(query)
                st.success("🎫 EventsBot found:")
                st.write(result)

        elif intent == "news":
            with st.spinner("Fetching latest news..."):
                result = handle_news(query)
                st.success("📰 Here's the news:")
                st.write(result)

        elif intent == "sports":
            with st.spinner("Checking sports updates..."):
                result = handle_sports(query)
                st.success("🏅 SportsBot reports:")
                st.write(result)

        else:
            st.info("⚙️ This intent is not supported yet. Try asking about travel or events.")