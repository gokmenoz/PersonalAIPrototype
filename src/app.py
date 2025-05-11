# app.py

import streamlit as st
from src.intent import detect_category_nova
from src.routers.travel_proxy import handle_travel
from src.routers.events_proxy import handle_events
from src.routers.news_proxy import handle_news
from src.routers.sports_proxy import handle_sports
# from src.routers.ai_proxy import handle_ai

st.set_page_config(page_title="🤖 EasyChat", layout="centered")
st.title("💬 Your Personal AI Assistant")

# Create two columns for the layout
col1, col2 = st.columns([2, 1])

with col1:
    query = st.text_input("Ask me anything:")

with col2:
    st.write("Or select a category:")
    travel_btn = st.button("🌍 Travel")
    events_btn = st.button("🎫 Events")
    news_btn = st.button("📰 News")
    sports_btn = st.button("🏅 Sports")

# Handle button clicks
if travel_btn:
    query = "Tell me about travel"
    intent = "travel"
elif events_btn:
    query = "Tell me about events"
    intent = "events"
elif news_btn:
    query = "Tell me about news"
    intent = "news"
elif sports_btn:
    query = "Tell me about sports"
    intent = "sports"
elif st.button("Submit"):
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

# Process the intent if we have one
if 'intent' in locals():
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