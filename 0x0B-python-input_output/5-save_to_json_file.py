#!/usr/bin/python3
"""Write an object to a text file using json."""
import json


def save_to_json_file(my_obj, filename):
    """Return a text file."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
