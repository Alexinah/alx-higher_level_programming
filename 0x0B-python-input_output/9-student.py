#!/usr/bin/python3
"""Class Student that defines a student by."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new student.

        Args:
        first_name (str): first name of the student
        last_name (str): last name of the studeny
        age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary representation of the Student."""
        return self.__dict__
