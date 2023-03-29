import json
from start_dialogue import start_dialogue
import yaml


def run():

    with open('sample_dialogues.yaml', 'r') as f:
        sample_dialogues = yaml.load(f, Loader=yaml.FullLoader)
    initial_prompt_a = sample_dialogues['novel']['initial_prompt_a']
    initial_prompt_b = sample_dialogues['novel']['initial_prompt_b']
    messages = start_dialogue(initial_prompt_a, initial_prompt_b)


if __name__ == '__main__':
    run()
