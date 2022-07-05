#!/usr/bin/python3
"""Function that writes a text file and returns the no of char"""


def write_file(filename="", text=""):
    """Writes and returns the no of characters
    Args:
        filename (str)
        text (str)
    Returns:
        The number of characters written.
        """
    with open(filename, "w", encoding="utf-8') as f:
        return f.write(text)
