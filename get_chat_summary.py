from get_chat_completion import get_chat_completion


def get_chat_summary(messages):
    
    summarization_prompt = f"""
        Could you summarize just the user responses in the below conversation for me?
        Please ignore messages from the assistant. 
        Please try to keep your response to under <2000 tokens
        Please try to use as few tokens as possible
        Please provide only the summary in your response and no superfluous text like 'Sure! I can hell with that' just to cut down on the size of the response

        Thank you!! I look forward to viewing your summary.

        Conversation:
        {str(messages)}
    """

    chat_summary = get_chat_completion([
        {'role': 'system', 'content': 'You are a helpful assistant.'}, 
        {'role': 'user', 'content': summarization_prompt}
    ])
    return chat_summary
