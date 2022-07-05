#!/usr/bin/python3
"""Returns am object"""
import json


def from_json_string(my_str):
    """Return an object from json"""
    return json.loads(my_str)
