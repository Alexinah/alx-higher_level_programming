#!/usr/bin/python3


def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    retu = list(a_dictionary.keys())[0]
    best = a_dictionary[retu]
    for i, j in a_dictionary.items():
        if j > best:
            best = j
            retu = i
    return (retu)
