import openai
import os
from get_selection import get_selection 
from dotenv import load_dotenv
import time
from spinner import Spinner

load_dotenv()
openai.api_key = os.environ['OPENAI_API_KEY']


def get_chat_completion(term, messages):
    with Spinner():
        completion = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=messages,
            n=3
        )
        options = [choice.message.content for choice in completion.choices]    
        # options = ["a", "b", "c"]

    key = ''
    selection = 0
    message = None
    while key != 'q':
        print(term.clear())
        for index, option in enumerate(options):
            preview_text = option[:60].replace('\n', '')
            option_text = f'{number_to_letter(index)} - {preview_text}'
            if index == selection:
                print(f'{term.yellow(option_text)}')
            else:
                print(f'{term.blue(option_text)}') 
        print(f'\n\n {options[selection]}')
        
        key = term.inkey()

        if hasattr(key, 'name'):
            if key.name == 'KEY_UP':
                selection = (selection - 1) % len(options)
            elif key.name == 'KEY_DOWN':
                selection = (selection + 1) % len(options)
            elif key.name == 'KEY_ENTER':
                message = options[selection]
                key = 'q'
        else:
            print(f'key {key} has no name attr')
    return message

def number_to_letter(number):
    return chr(number + 97)