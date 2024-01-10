#!/usr/bin/python3

class MyList(list):
    """Inherits from list and adds a method to print the list in sorted order."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))

