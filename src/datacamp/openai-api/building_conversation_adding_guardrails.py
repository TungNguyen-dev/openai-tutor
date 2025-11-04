import openai

OPENAI_BASE = "https://aiportalapi.stu-platform.live/jpe"
OPENAI_KEY = "sk-h6DB0Kzd1h5C45YYxtGAjw"
OPENAI_MODEL = "GPT-4o-mini"

# Create OpenAI client
client = openai.OpenAI(
    base_url=OPENAI_BASE,
    api_key=OPENAI_KEY
)

sys_msg = """
You are a study planning assistant that creates plans for learning new skills.

If these skills are non related to languages, return the message:
'Apologies, to focus on languages, we no longer create learning plans on other topics.'
"""

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": sys_msg},
        {"role": "user",
         "content": "Help me learn to a non-language-related skill, such as rollerskating.."}
    ]
)

print(response.choices[0].message.content)
