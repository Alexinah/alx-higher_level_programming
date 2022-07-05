#!/usr/bin/python3
"""Append a string to UTF8."""


def append_write(filename="", text=""):
    """Appends a string at the end of text file

    Args:
    filename (str): name of file
    text (str): text to append

    Returns:
    Number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
