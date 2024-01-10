#!/usr/bin/python3
"""Script to add all arguments to a Python list and save them to a file."""
import sys
from os import path
from json import dump, load
from pathlib import Path
from importlib import import_module


def save_to_json_file(my_obj, filename):
    """Save object to a JSON file."""
    with open(filename, 'w', encoding='utf-8') as file:
        dump(my_obj, file)


def load_from_json_file(filename):
    """Create an object from a JSON file."""
    with open(filename, 'r', encoding='utf-8') as file:
        return load(file)


filename = "add_item.json"

# Check if the file exists
if not path.isfile(filename):
    save_to_json_file([], filename)

# Load the list from the file
my_list = load_from_json_file(filename)

# Add command-line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(my_list, filename)

