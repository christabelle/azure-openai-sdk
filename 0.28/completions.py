import openai
import os

from dotenv import load_dotenv

# Get Configuration Settings
load_dotenv()

# Set OpenAI configuration settings
openai.api_type = "azure"
openai.api_base = os.getenv('AOAI_ENDPOINT_WE')
openai.api_version = "2023-05-15"
openai.api_key = os.getenv('AOAI_KEY_WE')

deployment_name = os.getenv('DEPLOYMENTS_WE')
deployment_name = deployment_name.split(',')[0].replace('"', '').replace('[', '').replace(']', '')
print("\nThe model in use is: " + deployment_name)

try:
    prompt = 'What is Azure OpenAI?'
    response = openai.Completion.create(engine=deployment_name, prompt=prompt,
                                        max_tokens=200, temperature=0.5)
    print("\nCompletion API Response:")
    print(response.choices[0].text)
except Exception as e:
    print("An error occurred: ", e)