import openai

OPENAI_BASE = "https://aiportalapi.stu-platform.live/jpe"
OPENAI_KEY = "sk-h6DB0Kzd1h5C45YYxtGAjw"
OPENAI_MODEL = "GPT-4o-mini"

# Create OpenAI client
client = openai.OpenAI(
    base_url=OPENAI_BASE,
    api_key=OPENAI_KEY
)

# Define a multi-line prompt to classify sentiment
prompt = """classify the sentiment of the statements provided using the numbers 1 to 5 (positive to negative):
1. Unbelievably good!
2. Shoes fell apart on the second use.
3. The shoes look nice, but they aren't very comfortable.
4. Can't wait to show them off!"""

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    max_completion_tokens=100
)

print(response.choices[0].message.content)
