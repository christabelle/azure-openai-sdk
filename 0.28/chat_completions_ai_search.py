import os
import openai
import requests

from dotenv import load_dotenv

# Get Configuration Settings
load_dotenv()

# Set OpenAI configuration settings
openai.api_type = "azure"
openai.api_base = os.getenv('AOAI_ENDPOINT_EUS')
# Azure OpenAI on your own data is only supported by the 2023-08-01-preview API version
openai.api_version = "2023-08-01-preview" 
openai.api_key = os.getenv('AOAI_KEY_EUS')

def setup_byod(deployment_id: str) -> None:
    """Sets up the OpenAI Python SDK to use your own data for the chat endpoint.
    :param deployment_id: The deployment ID for the model to use with your own data.
    To remove this configuration, simply set openai.requestssession to None.
    """

    class BringYourOwnDataAdapter(requests.adapters.HTTPAdapter):

     def send(self, request, **kwargs):
         request.url = f"{openai.api_base}/openai/deployments/{deployment_id}/extensions/chat/completions?api-version={openai.api_version}"
         return super().send(request, **kwargs)

    session = requests.Session()

    # Mount a custom adapter which will use the extensions endpoint for any call using the given `deployment_id`
    session.mount(
        prefix=f"{openai.api_base}/openai/deployments/{deployment_id}",
        adapter=BringYourOwnDataAdapter()
    )

    openai.requestssession = session

setup_byod("gpt-35-turbo-301")

response = openai.ChatCompletion.create(
    messages=[{"role": "user", "content": "Where can I stay in London?"}],
    deployment_id="gpt-35-turbo-301",
    dataSources=[  # camelCase is intentional, as this is the format the API expects
        {
            "type": "AzureCognitiveSearch",
            "parameters": {
                "endpoint": os.environ.get("SEARCH_ENDPOINT"),
                "key": os.environ.get("SEARCH_KEY"),
                "indexName": "margiestravel"
            }
        }
    ]
)

print(response['choices'][0]['message']['content'])
