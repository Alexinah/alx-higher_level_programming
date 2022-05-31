#!/usr/bin/python3

"""print numbers 0 - 98 in decimal and hexadecimal"""
for number in range(0, 99):
    print("{} = {}".format(number, hex(number)))
