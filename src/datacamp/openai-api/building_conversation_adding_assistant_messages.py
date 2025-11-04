import openai

OPENAI_BASE = "https://aiportalapi.stu-platform.live/jpe"
OPENAI_KEY = "sk-h6DB0Kzd1h5C45YYxtGAjw"
OPENAI_MODEL = "GPT-4o-mini"

# Create OpenAI client
client = openai.OpenAI(
    base_url=OPENAI_BASE,
    api_key=OPENAI_KEY
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    # Add a user and assistant message for in-context learning
    messages=[
        {
            "role": "system",
            "content": "You are a helpful Geography tutor that generates concise summaries for different countries."
        },
        {
            "role": "user",
            "content": "Give me a quick summary of Portugal."
        },
        {
            "role": "assistant",
            "content": "Portugal is a country in Europe that borders Spain. The capital city is Lisboa"
        },
        {
            "role": "user",
            "content": "Give me a quick summary of Greece."
        }
    ]
)

print(response.choices[0].message.content)
