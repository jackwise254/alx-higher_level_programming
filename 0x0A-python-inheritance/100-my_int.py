#!/usr/bin/python3
"""Module to define the MyInt class."""


class MyInt(int):
    """MyInt class that inherits from int."""

    def __eq__(self, other):
        """Override the == operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the != operator."""
        return super().__eq__(other)

