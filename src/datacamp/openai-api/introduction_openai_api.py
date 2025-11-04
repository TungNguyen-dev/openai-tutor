import openai

OPENAI_BASE = "https://aiportalapi.stu-platform.live/jpe"
OPENAI_KEY = "sk-h6DB0Kzd1h5C45YYxtGAjw"
OPENAI_MODEL = "GPT-4o-mini"

# Create openai client
client = openai.OpenAI(
    base_url=OPENAI_BASE,
    api_key=OPENAI_KEY
)

# Making request
response = client.chat.completions.create(
    model=OPENAI_MODEL,
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)

# ChatCompletion(
#     id='chatcmpl-CXr2oZBNBc4loi6jrvcRtDCUaCkVT',
#     object='chat.completion',
#     created=1762184762,
#     model='gpt-4o-mini-2024-07-18',
#     system_fingerprint='fp_efad92c60b',
#     service_tier=None,
#
#     choices=[
#         Choice(
#             index=0,
#             finish_reason='stop',
#             logprobs=None,
#             message=ChatCompletionMessage(
#                 role='assistant',
#                 content='Hello! How can I assist you today?',
#                 refusal=None,
#                 annotations=[],
#                 audio=None,
#                 function_call=None,
#                 tool_calls=None
#             ),
#             provider_specific_fields={
#                 'content_filter_results': {
#                     'hate': {'filtered': False, 'severity': 'safe'},
#                     'protected_material_code': {'filtered': False, 'detected': False},
#                     'protected_material_text': {'filtered': False, 'detected': False},
#                     'self_harm': {'filtered': False, 'severity': 'safe'},
#                     'sexual': {'filtered': False, 'severity': 'safe'},
#                     'violence': {'filtered': False, 'severity': 'safe'}
#                 }
#             }
#         )
#     ],
#
#     prompt_filter_results=[
#         {
#             'prompt_index': 0,
#             'content_filter_results': {
#                 'hate': {'filtered': False, 'severity': 'safe'},
#                 'jailbreak': {'filtered': False, 'detected': False},
#                 'self_harm': {'filtered': False, 'severity': 'safe'},
#                 'sexual': {'filtered': False, 'severity': 'safe'},
#                 'violence': {'filtered': False, 'severity': 'safe'}
#             }
#         }
#     ],
#
#     usage=CompletionUsage(
#         prompt_tokens=9,
#         completion_tokens=10,
#         total_tokens=19,
#         completion_tokens_details=CompletionTokensDetails(
#             accepted_prediction_tokens=0,
#             rejected_prediction_tokens=0,
#             reasoning_tokens=0,
#             audio_tokens=0
#         ),
#         prompt_tokens_details=PromptTokensDetails(
#             audio_tokens=0,
#             cached_tokens=0
#         )
#     )
# )
#
# # Message content:
# "Hello! How can I assist you today?"

