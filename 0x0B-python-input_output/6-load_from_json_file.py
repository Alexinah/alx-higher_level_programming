#!/usr/bin/python3
"""Function that creates an Object from JSON file"""


def load_from_json_file(filename):
    """Create an object from JSON"""
    with open(filename) as p:
        return json.load(p)
