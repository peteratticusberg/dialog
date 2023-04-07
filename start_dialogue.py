from tokens import get_token_count
from get_chat_completion import get_chat_completion
from datetime import datetime
import json


def start_dialogue(initial_prompt_a, initial_prompt_b):
    system_message = {'role': 'system', 'content': 'You are a helpful assistant.'}
    messages_a = [system_message]
    messages_b = [system_message]
    messages_a.append({'role': 'user', 'content': initial_prompt_a})
    messages_b.append({'role': 'user', 'content': initial_prompt_b})

    a_or_b = 'A'
    max_messages = 20
    approximate_token_usage = 0
    start_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    while len(messages_a) <= max_messages:

        messages_token_count = get_token_count(messages_a)
        approximate_token_usage += messages_token_count 
        
        print(f'message count: {len(messages_a)}')
        print(f'time: {datetime.now().strftime("%H:%M:%S")}')
        print(f'conversation size: {messages_token_count}')
        print(f'approximate token usage: {approximate_token_usage}')

        if a_or_b == 'A':
            message = get_chat_completion(messages_a)
            print(message)
            messages_a.append({'content': message, 'role': 'assistant'})
            messages_b.append({'content': message, 'role': 'user'})
            a_or_b = 'B'
        else:
            message = get_chat_completion(messages_b)
            print(message)
            messages_b.append({'content': message, 'role': 'assistant'})
            messages_a.append({'content': message, 'role': 'user'})
            a_or_b = 'A'

        with open(f"output/{start_time}.json", "w") as f:
            conversation_state = {
                'messages_a': messages_a,
                'messages_b': messages_b
            }
            f.write(json.dumps(conversation_state, indent=2))
                
    return messages_a
