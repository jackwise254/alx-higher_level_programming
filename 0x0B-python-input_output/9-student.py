#!/usr/bin/python3
"""Student module
"""

class Student:
    """Defines a student by first_name, last_name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """Instantiates a Student object with first_name, last_name, and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance.
        """
        # Get the dictionary representation of the object
        student_dict = self.__dict__.copy()
        return student_dict

