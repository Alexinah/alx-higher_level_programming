#!/usr/bin/python3


def uniq_add(my_list=[]):
    uniqueadd = 0

    for number in set(my_list):
        uniqueadd += number
    return(uniqueadd)
