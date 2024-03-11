import openai
import os

from dotenv import load_dotenv

# Get Configuration Settings
load_dotenv()

# Set OpenAI configuration settings
openai.api_type = "azure"
openai.api_base = os.getenv('AOAI_ENDPOINT_WE')
openai.api_version = "2023-03-15-preview"
openai.api_key = os.getenv('AOAI_KEY_WE')

deployment_name = 'gpt-35-turbo-301'

response = openai.Completion.create(
    engine=deployment_name,
    prompt="<|im_start|>system\nAssistant is a large language model trained by OpenAI.\n<|im_end|>\n<|im_start|>user\nWho were the founders of Microsoft?\n<|im_end|>\n<|im_start|>assistant\n",
    temperature=0,
    max_tokens=500,
    top_p=0.5,
    stop=["<|im_end|>"]
)
print("\n Chat Completion API")
print(response['choices'][0]['text'])
