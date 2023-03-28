import json
from start_dialogue import start_dialogue
from tokens import get_token_estimates


def run():
    with open('sample_dialogues.json', 'r') as f:
        sample_dialogues = json.load(f)
    initial_prompt_a = sample_dialogues.brain_chemistry.initial_prompt_a
    initial_prompt_b = sample_dialogues.brain_chemistry.initial_prompt_b
    messages = start_dialogue(initial_prompt_a, initial_prompt_b)
    print(get_token_estimates(messages))


if __name__ == '__main__':
    run()
