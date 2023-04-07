import openai
import os
from get_selection import get_selection 
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ['OPENAI_API_KEY']


def get_chat_completion(messages):
    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages,
        n=3
    )
    options = [choice.message.content for choice in completion.choices]
    message = get_selection(options)
    return message
