import openai
import os

from dotenv import load_dotenv
from utils_openai import completion, chat_completion, chat_conversation

def generate_response():
    # Get Configuration Settings
    load_dotenv()

    # Prompt user for input parameters
    region = input("Enter the region of the deployment (WE/EUS/CE): ")
    model_number = int(input("Enter the number of the model in the list of models (0,1,2): "))
    api_version = input("Enter the version of the API: ")
    api_type = input("Enter the type of API (chat/completion): ")

    endpoint = f'AOAI_ENDPOINT_{region.upper()}'
    key = f'AOAI_KEY_{region.upper()}'
    deployment = f'DEPLOYMENTS_{region.upper()}'

    # Set OpenAI configuration settings
    openai.api_type = "azure"
    openai.api_base = os.getenv(endpoint)
    openai.api_key = os.getenv(key)
    openai.api_version = api_version

    deployment_name = os.getenv(deployment)
    deployment_name = deployment_name.split(',')[model_number].replace('"', '').replace('[', '').replace(']', '')

    continuous = True

    if api_type == 'completion':
        completion(deployment_name)
    elif api_type == 'chat':
        if continuous:
            chat_conversation(deployment_name)
        else:
            chat_completion(deployment_name)
    else:
        print("Invalid API type. Please try again.")
   
if __name__ == '__main__':
    generate_response()