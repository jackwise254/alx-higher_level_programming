# models/base.py

import json

class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for Base class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""

        filename = cls.__name__ + ".json"
        json_str = "[]"

        if list_objs is not None:
            json_str = cls.to_json_string([obj.to_dictionary() for obj in list_objs])

        with open(filename, "w") as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of dictionaries represented by json_string"""

        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""

        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)  # Creating a dummy instance with minimum required attributes
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)  # Creating a dummy instance with minimum required attributes

        dummy_instance.update(**dictionary)  # Applying the real values using update method
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a file"""

        filename = cls.__name__ + ".json"

        try:
            with open(filename, "r") as file:
                json_str = file.read()
                dictionaries = cls.from_json_string(json_str)
                return [cls.create(**d) for d in dictionaries]
        except FileNotFoundError:
            return []

