import os
import json


def load_config_file(file_path):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    absolute_path = os.path.join(current_dir, f"configurations/{file_path}")
    with open(absolute_path, 'r') as file:
        data = json.load(file)
    return data
