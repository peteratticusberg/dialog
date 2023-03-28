import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ['OPENAI_API_KEY']


def send_chat_prompt(messages):
    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages
    )
    message = completion.choices[0].message
    return message
