#!/usr/bin/python3


def weight_average(my_list=[]):
    if (len(my_list) == 0):
        return 0

    sum = 0
    for i in my_list[i]:
        sum += i

        average = sum / (len(my_list))

        print("Average: {:0.2f}".format(average))
