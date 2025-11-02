import openai

OPENAI_BASE = "https://aiportalapi.stu-platform.live/jpe"
OPENAI_KEY = "sk-QBHCHee4dfkLTgE_RjAB5Q"
OPENAI_MODEL = "GPT-4o-mini"

client = openai.OpenAI(
    base_url=OPENAI_BASE,
    api_key=OPENAI_KEY
)

response = client.chat.completions.create(
    model=OPENAI_MODEL,
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)
