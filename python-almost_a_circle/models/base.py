#!/usr/bin/python3
"""Defines Base, the base class that manages ids for all shapes."""
import json


class Base:
    """Base of all shapes: assigns ids and handles JSON serialization."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Sets id to the given value, or to the next automatic id."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string of a list of dictionaries, or "[]"."""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list represented by a JSON string, or an empty list."""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON representation of list_objs to <Class name>.json."""
        dicts = [obj.to_dictionary() for obj in list_objs or []]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(dicts))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance of cls with all attributes set by update."""
        if cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns the list of instances stored in <Class name>.json."""
        try:
            with open("{}.json".format(cls.__name__), encoding="utf-8") as f:
                dicts = cls.from_json_string(f.read())
        except FileNotFoundError:
            return []
        return [cls.create(**d) for d in dicts]
