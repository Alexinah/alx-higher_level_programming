#!/usr/bin/python3


def best_score(a_dictionary):
    for i in a_dictionary:
        if i  > a_dictionary[i]:
            return i
        else:
            return None
