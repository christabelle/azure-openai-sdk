# Packages required:
import requests 
import json
import os

from dotenv import load_dotenv

# Get Configuration Settings
load_dotenv()

api_base = os.getenv('AOAI_ENDPOINT_SC')
api_key = os.getenv('AOAI_KEY_SC')
deployment_name = 'gpt-4-vision-preview'

base_url = f"{api_base}openai/deployments/{deployment_name}" 
headers = {   
    "Content-Type": "application/json",   
    "api-key": api_key 
}

# Prepare endpoint, headers, and request body 
endpoint = f"{base_url}/chat/completions?api-version=2023-12-01-preview"

data = {
    "model": "gpt-4-vision-preview",
    "enhancements": {
        "ocr": {
          "enabled": True
        },
        "grounding": {
          "enabled": True
        }
    },
    "messages": [
        {
            "role": "system", 
            "content": "You are a helpful assistant."
        }, 
        {
            "role": "user", 
            "content": [  
                { 
                    "type": "text", 
                    "text": "Describe this picture:" 
                },
                { 
                    "type": "image_url", 
                    "image_url": {
                        "url" : os.getenv('BLOB_IMAGE_URL')
                    }
                }
        ]} 
    ], 
    "max_tokens": 2000,
    "stream": False
}   

# Make the API call   
response = requests.post(endpoint, headers=headers, data=json.dumps(data))   

if response.status_code == 200:
    try:
        res = response.json()
        print(f'Response: {res["choices"][0]["message"]["content"]}')
    except ValueError:
        print('Error: response content could not be parsed as JSON')
else:
    print(f'Error: HTTP {response.status_code} - {response.reason}')