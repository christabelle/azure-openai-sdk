import openai
import os

from dotenv import load_dotenv

# Get Configuration Settings
load_dotenv()

# Set OpenAI configuration settings
openai.api_type = "azure"
openai.api_base = os.getenv('AOAI_ENDPOINT_EUS')
openai.api_version = "2023-03-15-preview"
openai.api_key = os.getenv('AOAI_KEY_EUS')

deployment_name = 'gpt-35-turbo-301'

response = openai.ChatCompletion.create(
    engine=deployment_name,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Does Azure OpenAI support multiple languages?"},
        {"role": "assistant", "content": "Yes, Azure OpenAI supports several languages, and can translate between them."},
        {"role": "user", "content": "Do other Azure AI Services support translation too?"}
    ]
)
print("\nChat Completion API")
print(response['choices'][0]['message']['content'])
