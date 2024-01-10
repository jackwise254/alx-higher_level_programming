#!/usr/bin/python3
"""Module to define the write_file function."""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF8) and return the number of characters written."""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)

