from tokens import get_token_count
from send_chat_prompt import send_chat_prompt
from datetime import datetime


def start_dialogue(initial_prompt_a, initial_prompt_b):
    system_message = {'role': 'system', 'content': 'You are a helpful assistant.'}
    messages_a = [system_message]
    messages_b = [system_message]
    messages_a.append({'role': 'user', 'content': initial_prompt_a})
    messages_b.append({'role': 'user', 'content': initial_prompt_b})

    a_or_b = 'A'
    max_messages = 20
    approximate_token_usage = 0
    while len(messages_a) <= max_messages:

        messages_token_count = get_token_count(messages_a)
        approximate_token_usage += messages_token_count 
        
        print(f'message count: {len(messages_a)}')
        print(f'time: {datetime.now().strftime("%H:%M:%S")}')
        print(f'approximate token usage: {approximate_token_usage}')

        if a_or_b == 'A':
            message = send_chat_prompt(messages_a)
            print(message['content'])
            messages_a.append({**message})
            messages_b.append({**message, 'role': 'user'})
            a_or_b = 'B'
        else:
            message = send_chat_prompt(messages_b)
            print(message['content'])
            messages_b.append({**message})
            messages_a.append({**message, 'role': 'user'})
            a_or_b = 'A'

    return messages_a
