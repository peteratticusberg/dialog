from tokens import get_token_count
from get_chat_completion import get_chat_completion
from datetime import datetime
import json
import blessed


def start_dialogue(initial_prompt_a, initial_prompt_b):
    system_message = {'role': 'system', 'content': 'You are a helpful assistant.'}
    messages_a = [system_message, {'role': 'user', 'content': initial_prompt_a}]
    messages_b = [system_message, {'role': 'user', 'content': initial_prompt_b}]

    term = blessed.Terminal()    
    with term.cbreak():
        a_or_b = 'A'
        approximate_token_usage = 0
        key = 'c' 
        while key != 'q':
            # print('press q to quit, c to continue, or s for stats')
            # print(term)
            # key = term.inkey()
            if key == 'c':
                approximate_token_usage += get_token_count(messages_a)
                message = get_chat_completion(term, get_messages(a_or_b, messages_a, messages_b))    
                log_message(a_or_b, message, messages_a, messages_b)
                log_turn(messages_a, messages_b)
                a_or_b = toggle(a_or_b)
            elif key == 's':
                print(f'current conversation size is {get_token_count(messages_a)}.')
                print(f'estimated token usage is {approximate_token_usage}')
                print(f'conversation is {len(messages_a)} messages long.')


def get_messages(a_or_b, messages_a, messages_b):
    return messages_a if a_or_b == 'A' else messages_b


def toggle(a_or_b):
    return 'B' if a_or_b == 'A' else 'B'


def log_message(a_or_b, message, messages_a, messages_b):
    if a_or_b == 'A':
        messages_a.append({'content': message, 'role': 'assistant'})
        messages_b.append({'content': message, 'role': 'user'})
    else:
        messages_b.append({'content': message, 'role': 'assistant'})
        messages_a.append({'content': message, 'role': 'user'})

start_time = datetime.now().strftime("%Y%m%d_%H%M%S")
def log_turn(messages_a, messages_b):
    with open(f"output/{start_time}.json", "w") as f:
        conversation_state = {
            'messages_a': messages_a,
            'messages_b': messages_b
        }
        f.write(json.dumps(conversation_state, indent=2))

# print(f'message count: {len(messages_a)}')
# print(f'time: {datetime.now().strftime("%H:%M:%S")}')
# print(f'conversation size: {messages_token_count}')
# print(f'approximate token usage: {approximate_token_usage}')
