import os

from dotenv import load_dotenv
from openai import AzureOpenAI

# Get Configuration Settings
load_dotenv()

# Set OpenAI configuration settings
client = AzureOpenAI(
    api_key=os.getenv("AOAI_KEY_EUS"),  
    api_version="2023-03-15-preview",
    azure_endpoint = os.getenv("AOAI_ENDPOINT_EUS")
    )

deployment_name = 'gpt-35-turbo-301'

response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
        {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
        {"role": "user", "content": "Do other Azure AI services support this too?"}
    ]
)

print("\nChat Completion API")
print(response.choices[0].message.content)
