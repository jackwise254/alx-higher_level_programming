#!/usr/bin/python3
"""Module to define the read_file function."""


def read_file(filename=""):
    """Read and print the content of a text file (UTF8)."""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")

