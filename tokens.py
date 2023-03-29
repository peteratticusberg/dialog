import tiktoken


def get_token_count(messages):
    full_content = " ".join([message['content'] for message in messages])
    encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(full_content))
