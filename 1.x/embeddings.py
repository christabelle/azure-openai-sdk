import os
from dotenv import load_dotenv
from openai import AzureOpenAI

# Get Configuration Settings
load_dotenv()

client = AzureOpenAI(
  api_key = os.getenv("AOAI_KEY_WE"),  
  api_version = "2023-05-15",
  azure_endpoint =os.getenv("AOAI_ENDPOINT_WE") 
)

response = client.embeddings.create(
    input = "Your text string goes here",
    model= "text-embedding-ada-002-2"  
)

print(response.model_dump_json(indent=2))