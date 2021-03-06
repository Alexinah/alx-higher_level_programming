#!/usr/bin/python3
"""Function that writes a text file and returns the no of char"""


def write_file(filename="", text=""):
    """Writes and returns the no of characters
    Args:
        filename (str): The name of the file to write
        text (str): The text to write to the file
    Returns:
        The number of characters written.
        """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
