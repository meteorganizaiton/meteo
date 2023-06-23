import os
import json


def load_config_file(file_path):
    # Get the absolute path to the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Combine the current directory and the relative file path
    absolute_path = os.path.join(current_dir, f"configurations/{file_path}")

    # Load the JSON file
    with open(absolute_path, 'r') as file:
        data = json.load(file)

    return data
