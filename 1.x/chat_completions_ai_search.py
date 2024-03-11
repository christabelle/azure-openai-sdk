import os
import openai
import requests

from dotenv import load_dotenv

# Get Configuration Settings
load_dotenv()

endpoint = os.environ.get("AOAI_ENDPOINT_EUS")
api_key = os.environ.get("AOAI_KEY_EUS")
deployment = "gpt-35-turbo-301"

client = openai.AzureOpenAI(
    base_url=f"{endpoint}/openai/deployments/{deployment}/extensions",
    api_key=api_key,
    api_version="2023-08-01-preview",
)

response = client.chat.completions.create(
    model=deployment,
    messages=[
        {
            "role": "user",
            "content": "I'm traveling to New York and need to find a hotel.",
        },
    ],
    extra_body={
        "dataSources": [
            {
                "type": "AzureCognitiveSearch",
                "parameters": {
                    "endpoint": os.environ["SEARCH_ENDPOINT"],
                    "key": os.environ["SEARCH_KEY"],
                    "indexName": "margiestravel"
                }
            }
        ]
    }
)

print(response.model_dump_json(indent=2))