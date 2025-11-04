import openai

OPENAI_BASE = "https://aiportalapi.stu-platform.live/jpe"
OPENAI_KEY = "sk-h6DB0Kzd1h5C45YYxtGAjw"
OPENAI_MODEL = "GPT-4o-mini"

# Create OpenAI client
client = openai.OpenAI(
    base_url=OPENAI_BASE,
    api_key=OPENAI_KEY
)

# -- SUMMARIZING & EDITING TEXT --
# Text summarization
finance_text = """
"""

# Use an f-string to format the prompt
prompt = f"""Summarize the following text into two concise bullet points:
{finance_text}"""

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    max_completion_tokens=400
)

print(response.choices[0].message.content)
