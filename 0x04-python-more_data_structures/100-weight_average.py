#!/usr/bin/python3


def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return 0

    add = 0
    size = len(my_list)
    for tup in my_list:
        add += (tup[0] * tup[1])
        return (add / size)
