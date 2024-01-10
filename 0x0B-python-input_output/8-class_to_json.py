#!/usr/bin/python3
"""Class to JSON module
"""

def class_to_json(obj):
    """Returns the dictionary description with simple data structure for JSON serialization."""
    # Get the dictionary representation of the object
    obj_dict = obj.__dict__.copy()

    # Handle special cases for class attributes (e.g., class variables)
    if hasattr(obj, '__class__'):
        class_attributes = [attr for attr in dir(obj.__class__) if not callable(getattr(obj.__class__, attr)) and not attr.startswith("__")]
        for attr in class_attributes:
            if hasattr(obj, attr):
                obj_dict[attr] = getattr(obj, attr)

    return obj_dict

