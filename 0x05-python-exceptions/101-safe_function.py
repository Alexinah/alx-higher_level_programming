#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """ Function that executes a function safely."""
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=stderr)
        return (None)
