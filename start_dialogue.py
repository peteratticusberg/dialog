from tokens import get_token_estimates
from send_chat_prompt import send_chat_prompt
from datetime import datetime


def start_dialogue(initial_prompt_a, initial_prompt_b):
    system_message = {'role': 'system', 'content': 'You are a helpful assistant.'}
    messages_a = [system_message]
    messages_b = [system_message]
    messages_a.append({'role': 'user', 'content': initial_prompt_a})
    messages_b.append({'role': 'user', 'content': initial_prompt_b})

    print('messagesA:')
    print(messages_a)

    a_or_b = 'A'
    max_messages = 20
    while len(messages_a) <= max_messages:
        print(f'\n\n message count: {len(messages_a)} time: {datetime.now().strftime("%H:%M:%S")} {get_token_estimates(messages_a)} \n\n')
        if a_or_b == 'A':
            message = send_chat_prompt(messages_a)
            print(message.content)
            messages_a.append({**message})
            messages_b.append({**message, 'role': 'user'})
            a_or_b = 'B'
        else:
            message = send_chat_prompt(messages_b)
            print(message.content)
            messages_b.append({**message})
            messages_a.append({**message, 'role': 'user'})
            a_or_b = 'A'
            # await sleep(5)

    return messages_a