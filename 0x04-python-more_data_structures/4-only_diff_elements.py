#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    """in 1 or 2 but not in both"""
    return (set_1 ^ set_2)
