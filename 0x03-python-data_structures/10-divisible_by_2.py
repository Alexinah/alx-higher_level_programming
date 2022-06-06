#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """Finds all multiples of 2"""
    for i in range len(my_list):
        if i % 2 == 0:
            print("{:d} {:s} divisible by 2".format(my_list[i]))
    else:
        print("{:d} is not divisible by 2".format(my_list[i]))
