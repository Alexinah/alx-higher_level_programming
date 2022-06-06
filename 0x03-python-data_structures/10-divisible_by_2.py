#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """Finds all multiples of 2"""
    for i in range(len(my_list):
        if my_list[i] % 2 == 0:
            print("{:d} {:s} divisible by 2".format(my_list[i], "is"
                    if my_list[i] else "is not"))
