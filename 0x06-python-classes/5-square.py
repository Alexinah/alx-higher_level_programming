#!/usr/bin/python3
"""Defines a square."""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Initializes an instance of a class"""

        @property
        def size(self):
            """GEt the current size of the square"""
            return (self.__size)

        @size.setters
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

        def area(self):
            """Return the current area of the square."""
            return (self.__size * self.__size)

        def my_print(self):
            """Print the square with # character."""
            for i in range(0, self.__size):
                [print("#", end="") for j in range(self.__size)]
                print("")
                if self.__size == 0:
                    print("")
