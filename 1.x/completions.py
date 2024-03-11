import os
from dotenv import load_dotenv
from openai import AzureOpenAI

# Get Configuration Settings
load_dotenv()
    
client = AzureOpenAI(
    api_key=os.getenv("AOAI_KEY_EUS"),  
    api_version="2023-12-01-preview",
    azure_endpoint = os.getenv("AOAI_ENDPOINT_EUS")
)
    
deployment_name='gpt-35-turbo-301' #This will correspond to the custom name you chose for your deployment when you deployed a model. 
    
# Send a completion call to generate an answer
print('Sending a test completion job')
start_phrase = 'Write a tagline for an ice cream shop. '
response = client.completions.create(model=deployment_name, prompt=start_phrase, max_tokens=20)
print(response.choices[0].text)