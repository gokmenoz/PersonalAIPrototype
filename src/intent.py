import boto3
import json

session = boto3.Session(profile_name="ogokmen_bedrock")
bedrock = session.client("bedrock-runtime", region_name="us-east-1")

MODEL_ID = "amazon.nova-lite-v1:0"
CATEGORIES = ["travel", "ai", "sports", "events", "news"]

FEW_SHOT_EXAMPLES = [
    ("I’m planning a trip to Italy, what should I see?", "travel"),
    ("Tell me the latest news about elections.", "news"),
    ("How did the Lakers do last night?", "sports"),
    ("Is GPT-4 better than Claude?", "ai"),
    ("Are there any live concerts in Berlin this weekend?", "concerts"),
]

def detect_category_nova(user_input: str, retries=3):
    # Prepare few-shot messages
    messages = []

    # System prompt (optional)
    messages.append({
        "role": "user",
        "content": [{"text": (
            f"You are an intent classifier. Respond with just one of: {', '.join(CATEGORIES)}. "
            "No extra explanation or text, just the category name."
        )}]
    })

    # Few-shot examples
    for example_input, example_label in FEW_SHOT_EXAMPLES:
        messages.append({
            "role": "user",
            "content": [{"text": f"{example_input}"}]
        })
        messages.append({
            "role": "assistant",
            "content": [{"text": example_label}]
        })

    # Actual user query
    messages.append({
        "role": "user",
        "content": [{"text": user_input}]
    })

    payload = {
        "inferenceConfig": {
            "max_new_tokens": 5,
            "temperature": 0.0
        },
        "messages": messages
    }

    for _ in range(retries):
        try:
            response = bedrock.invoke_model(
                modelId=MODEL_ID,
                contentType="application/json",
                accept="application/json",
                body=json.dumps(payload),
            )
            body = json.loads(response["body"].read())
            text = body["output"]["message"]["content"][0]["text"].strip().lower()
            return text if text in CATEGORIES else "unknown"
        except Exception as e:
            print(f"⚠️ Nova classification error: {e}")
            continue

    return "unknown"