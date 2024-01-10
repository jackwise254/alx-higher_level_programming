#!/usr/bin/python3
"""Module to define the from_json_string function."""
import json


def from_json_string(my_str):
    """Return an object represented by a JSON string."""
    return json.loads(my_str)

