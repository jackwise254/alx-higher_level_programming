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

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.
        """
        # If attrs is a list of strings, only retrieve the specified attributes
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            student_dict = {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        else:
            # If attrs is not a valid list, retrieve all attributes
            student_dict = self.__dict__.copy()
        
        return student_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.
        """
        for key, value in json.items():
            setattr(self, key, value)

