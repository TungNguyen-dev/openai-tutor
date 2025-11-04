import openai

OPENAI_BASE = "https://aiportalapi.stu-platform.live/jpe"
OPENAI_KEY = "sk-h6DB0Kzd1h5C45YYxtGAjw"
OPENAI_MODEL = "GPT-4o-mini"

# Create OpenAI client
client = openai.OpenAI(
    base_url=OPENAI_BASE,
    api_key=OPENAI_KEY
)

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
    model="gpt-4o-mini",
    max_completion_tokens=150,
    messages=[
        {
            "role": "system",
            "content": "You are a study planning assistant that creates plans for learning new skills."
        },
        {
            "role": "user",
            "content": "I want to learn to speak Dutch."
        }
    ]
)

#  Extract the assistant's text response
print(response.choices[0].message.content)
