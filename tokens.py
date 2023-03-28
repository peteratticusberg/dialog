import tiktoken


def get_token_estimate(messages):
    full_content = " ".join([message.content for message in messages])
    encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(full_content))


def get_token_usage_estimate(messages):
    token_estimate = get_token_estimate(messages)
    return token_estimate * len(messages) / 2


def get_token_cost_estimate(messages):
    token_usage_estimate = get_token_estimate(messages)
    return token_usage_estimate / 1000 * 0.002


def get_token_estimates(messages):
    return {
        "token_count": get_token_estimate(messages),
        "token_usage_estimate": get_token_usage_estimate(messages),
        "token_cost_estimate": get_token_cost_estimate(messages),
    }
