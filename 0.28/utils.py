import tiktoken

def create_chatml(display=False):
    """Creates a list of messages in chatML format.
    
    <|im_start|>system 
    Provide some context and/or instructions to the model.
    <|im_end|> 
    <|im_start|>user 
    The user’s message goes here
    <|im_end|> 
    <|im_start|>assistant 
    
    """
    system_message = input("Enter a system message: ")
    messages = f"<|im_start|>system\n{system_message}<|im_end|>"
    user_flag = True

    while True:
        message = input("Enter a user/assistant message (Press Enter to finish): ")
        if not message:
            break
        else:
            sender = 'user' if user_flag else 'assistant'
            messages += f"\n<|im_start|>{sender}\n{message}<|im_end|>"
    messages += "\n<|im_start|>assistant\n"

    if display:
        print('\nThis is the ChatML prompt:\n\n', messages)
    return messages.strip()

def create_messages():
    """Creates a list of messages in the format required by the API.
    
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is Azure OpenAI?"}
    ]    
    """
    user_flag = True
    messages = []
    message = input("Enter a system message: ")
    messages.append({"role": "system", "content": message})
    while True:
        message = input("Enter a user/assistant message (Press Enter to end): ")
        if not message:
            break
        else:
            sender = 'user' if user_flag else 'assistant'
            messages.append({"role": sender, "content": message})
    return messages

def num_tokens_from_messages(messages):
    # model to encoding mapping https://github.com/openai/tiktoken/blob/main/tiktoken/model.py
    encoding= tiktoken.get_encoding("cl100k_base")
    num_tokens = 0
    for message in messages:
        num_tokens += 4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":  # if there's a name, the role is omitted
                num_tokens += -1  # role is always required and always 1 token
    num_tokens += 2  # every reply is primed with <im_start>assistant
    return num_tokens