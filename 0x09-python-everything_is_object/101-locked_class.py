#!/usr/bin/python3
""" Defines class LockedClass that prevents user from
    creating new instance attributes"""


class LockedClasss:
    __slots__ = ["first_name"]

    def __init__(self):
        """Initialized an object of a class"""
        pass
