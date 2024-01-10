#!/usr/bin/python3
"""Module to define the add_attribute function."""


def add_attribute(obj, attribute, value):
    """Add attribute to object if it's possible."""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)

