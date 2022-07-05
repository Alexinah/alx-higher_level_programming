#!/usr/bin/python3
"""Function that creates an Object from JSON file"""
import json


def load_from_json_file(filename):
    """Create an object from JSON"""
    with open(filename) as f:
        return json.load(f)
