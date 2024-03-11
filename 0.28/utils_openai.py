import openai

from utils import create_chatml, create_messages, num_tokens_from_messages

TOKEN_SIZE = {'gpt-35-turbo': 4096, 'gpt-4': 8192, 'gpt-4-32k': 327}

def completion(deployment_name):
    try:
        check = input("Do you want to use chat prompt? (Y/N): ")
        if check == 'N':
            prompt = input("Enter a prompt: ")
        elif check == 'Y':
            display = input("Do you want to display the chat prompt (Y/N): ")
            display = True if display == 'Y' else False
            prompt = create_chatml(display)

        max_tokens = int(input("Enter the max tokens: "))
        temperature = float(input("Enter the temperature: "))
        print("\nThe model in use is: " + deployment_name)
        response = openai.Completion.create(engine=deployment_name, prompt=prompt, 
                                            max_tokens=max_tokens, temperature=temperature)
        print("\nCompletion API Response:")
        print(response.choices[0].text)
    except Exception as e:
        print("An error occurred: ", e)

def chat_completion(deployment_name):
    try:
        check = input("Do you want to create a new message prompt? (Y/N): ")
        if check == 'Y':
            messages = create_messages()
        else:
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "What is Azure OpenAI?"}
            ]
        
        # Process the messages
        if messages:
            max_tokens = int(input("Enter the max tokens: "))
            temperature = float(input("Enter the temperature: "))
            print("\nThe model in use is: " + deployment_name)
            
            response = openai.ChatCompletion.create(
                engine=deployment_name,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature)
            
            print("\nChat Completion API")
            print(response['choices'][0]['message']['content'])
        else:
            print("No message found. Please try again.")
    except Exception as e:
        print("An error occurred: ", e)

def chat_conversation(deployment_name):
    conversation = []
    try:
        token_limit = next((TOKEN_SIZE[token_size] for token_size in TOKEN_SIZE.keys() if deployment_name[:deployment_name.rfind('-')] == token_size), None)
        max_tokens = int(input("Enter the max tokens: "))
        temperature = float(input("Enter the temperature: "))
        print("\nThe model in use is: " + deployment_name)
        message = input("Enter a system message: ")
        conversation.append({"role": "system", "content": message})

        while True:
            message = input("Enter a user message (Press Enter to end conversation): ")  
            if not message:
                break  
            conversation.append({"role": "user", "content": message})

            conv_history_tokens = num_tokens_from_messages(conversation)

            while conv_history_tokens + max_tokens >= token_limit:
                print('Conversation token limit reached. Removing oldest message.')
                del conversation[1] 
                conv_history_tokens = num_tokens_from_messages(conversation)

            response = openai.ChatCompletion.create(
                engine = deployment_name,
                messages = conversation,
                max_tokens = max_tokens,
                temperature = temperature
            )

            print("\n" + response['choices'][0]['message']['content'] + "\n")
            print("\nCurrent conversation token rate is " + str(round(((conv_history_tokens/token_limit)*100), 2)) + "%")
            print("Number of messages in conversation: " + str(len(conversation)))
            conversation.append({"role": "assistant", "content": response["choices"][0]["message"]["content"]})
        
    except Exception as e:
        print("An error occurred: ", e)